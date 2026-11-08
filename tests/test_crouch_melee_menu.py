"""Execute the compiled shortcut, Travel cleanup and menu resource lifecycle.

Raw input and native button effects are supplied by the harness. These tests
exercise emitted script actions, not native Overwatch input or animation timing.
"""

from copy import deepcopy
import unittest

from tests.test_global_spectator_rejoin import ARTIFACT, SpectatorRuntimeEvaluator
from tests.test_fly_motion import Vector
from tools import validate_global_runtime as runtime


class ShortcutRuntimeEvaluator(SpectatorRuntimeEvaluator):
    def __init__(self, source):
        self.button_actions = []
        self.kills = []
        super().__init__(source)

    def call(self, name, args):
        if name == "IsMeleeing":
            return self.players[args[0]].get("melee", False)
        if name == "EyePosition":
            return self.players[args[0]]["position"] + Vector(0, 1.6, 0)
        if name in ("IsInViewAngle", "IsInLineOfSight"):
            return True  # Supply native geometry queries; do not model a map.
        return super().call(name, args)

    def native(self, name, arguments):
        if name == "Kill":
            from tools import validate_workshop as semantic
            args = semantic.split_top_level(arguments, ",")
            target, attacker = (self.expression(arg) for arg in args)
            self.kills.append((target, attacker))
            self.players[target]["alive"] = False
            return
        if name in ("AllowButton", "DisallowButton"):
            from tools import validate_workshop as semantic
            args = semantic.split_top_level(arguments, ",")
            self.button_actions.append((name, self.expression(args[0]),
                                        self.expression(args[1])))
        super().native(name, arguments)

    def input(self, owner, held, now=None):
        self.players[owner]["held"] = set(held)
        self.now = self.now + 0.05 if now is None else now
        self.globals.update(TriggerPlayer=owner, ActivePlayer=owner)
        self.run("ProcessGlobalController")


class CrouchMeleeMenuTests(unittest.TestCase):
    def model(self, **changes):
        model = ShortcutRuntimeEvaluator(runtime.english(ARTIFACT.read_text(encoding="utf-8")))
        owner = model.ready_player("owner", **changes)
        return model, owner

    def test_combo_opens_immediately_without_a_half_second_hold(self):
        model, owner = self.model()
        model.input("owner", {"Crouch", "Melee"}, now=10)
        self.assertTrue(owner["MenuOpen"])
        self.assertEqual(owner["MenuPage"], -1)
        self.assertTrue(owner["MeleeConsumed"])
        self.assertIn(owner["MenuHud"], model.resources)

    def test_melee_alone_never_opens_or_closes_the_menu(self):
        for opened in (False, True):
            with self.subTest(opened=opened):
                model, owner = self.model()
                if opened:
                    model.input("owner", {"Crouch", "Melee"})
                    model.input("owner", set())
                original_hud = owner["MenuHud"]
                for now in (10, 10.1, 10.5, 12):
                    model.input("owner", {"Melee"}, now=now)
                    self.assertEqual(owner["MenuOpen"], opened)
                    self.assertEqual(owner["MenuHud"], original_hud)

    def test_crouch_first_can_replace_an_active_travel_hud(self):
        model, owner = self.model(CrouchTravelEnabled=True)
        model.input("owner", {"Crouch"})
        self.assertTrue(owner["CrouchTravelActive"])
        old_hud = owner["MenuHud"]
        before = len(model.native_log)
        model.input("owner", {"Crouch", "Melee"})
        self.assertTrue(owner["MenuOpen"])
        self.assertFalse(owner["CrouchTravelActive"])
        self.assertIn(old_hud, model.destroyed)
        self.assertNotEqual(owner["MenuHud"], old_hud)
        self.assertIn(owner["MenuHud"], model.resources)
        self.assertEqual(model.globals["MenuHudIds"][0], owner["MenuHud"])
        events = model.native_log[before:]
        destroy = next(i for i, item in enumerate(events)
                       if item[1:] == ("DestroyHUDText", old_hud))
        create = next(i for i, item in enumerate(events) if item[1] == "CreateHUDText")
        self.assertLess(destroy, create)

    def test_simultaneous_combo_has_priority_over_travel_opening(self):
        model, owner = self.model(CrouchTravelEnabled=True)
        model.input("owner", {"Crouch", "Melee"})
        self.assertTrue(owner["MenuOpen"])
        self.assertFalse(owner["CrouchTravelActive"])

    def test_held_melee_cannot_toggle_again_by_repressing_crouch(self):
        model, owner = self.model()
        model.input("owner", {"Crouch", "Melee"})
        hud = owner["MenuHud"]
        for held in ({"Crouch", "Melee"}, {"Melee"}, {"Crouch", "Melee"}):
            model.input("owner", held)
            self.assertTrue(owner["MenuOpen"])
            self.assertEqual(owner["MenuHud"], hud)

    def test_melee_pressed_before_crouch_also_opens_the_combo_once(self):
        model, owner = self.model()
        model.input("owner", {"Melee"})
        self.assertFalse(owner["MenuOpen"])
        model.input("owner", {"Crouch", "Melee"})
        self.assertTrue(owner["MenuOpen"])
        model.input("owner", {"Crouch", "Melee"})
        self.assertTrue(owner["MenuOpen"])

    def test_melee_release_rearms_one_close_and_one_new_open(self):
        model, owner = self.model()
        model.input("owner", {"Crouch", "Melee"})
        first_hud = owner["MenuHud"]
        model.input("owner", {"Crouch"})
        model.input("owner", {"Crouch", "Melee"})
        self.assertFalse(owner["MenuOpen"])
        self.assertIn(first_hud, model.destroyed)
        self.assertTrue(owner["MeleeConsumed"])
        model.input("owner", {"Crouch", "Melee"})
        self.assertFalse(owner["MenuOpen"])
        model.input("owner", {"Crouch"})
        model.input("owner", {"Crouch", "Melee"})
        self.assertTrue(owner["MenuOpen"])
        self.assertNotEqual(owner["MenuHud"], first_hud)

    def test_closing_while_travel_is_enabled_does_not_open_travel_in_the_same_tick(self):
        model, owner = self.model(CrouchTravelEnabled=True)
        model.input("owner", {"Crouch", "Melee"})
        model.input("owner", {"Crouch"})
        model.input("owner", {"Crouch", "Melee"})
        self.assertFalse(owner["MenuOpen"])
        self.assertFalse(owner["CrouchTravelActive"])
        self.assertIsNone(owner["MenuHud"])

    def test_dead_owner_cannot_open_or_close_and_alive_input_rearms(self):
        for opened in (False, True):
            with self.subTest(opened=opened):
                model, owner = self.model()
                if opened:
                    model.input("owner", {"Crouch", "Melee"})
                    model.input("owner", set())
                owner["alive"] = False
                hud = owner["MenuHud"]
                model.input("owner", {"Crouch", "Melee"})
                self.assertEqual(owner["MenuOpen"], opened)
                self.assertEqual(owner["MenuHud"], hud)
                model.input("owner", set())
                owner["alive"] = True
                model.input("owner", {"Crouch", "Melee"})
                self.assertEqual(owner["MenuOpen"], not opened)

    def test_combo_is_owned_and_does_not_change_another_players_menu(self):
        model, owner = self.model()
        other = model.ready_player("other")
        saved = deepcopy(other)
        model.input("owner", {"Crouch", "Melee"})
        self.assertTrue(owner["MenuOpen"])
        self.assertEqual(other, saved)

    def punch_lobby(self, opened=False, protected=False):
        model, owner = self.model(CrouchTravelEnabled=True)
        if opened:
            model.input("owner", {"Crouch", "Melee"})
            model.input("owner", set())
        target = model.ready_player("target", position=Vector(2, 5, 9),
                                    UnkillableActive=protected,
                                    UnkillableMode=1 if protected else 0)
        model.globals["SuperPunchPlayers"] = ["owner"]
        model.globals["SuperPunchTimes"][int(owner["HudSlot"])] = 0
        return model, owner, target

    def test_same_combo_toggles_menu_and_scanned_punch_kills_once(self):
        for opened in (False, True):
            with self.subTest(opened=opened):
                model, owner, target = self.punch_lobby(opened=opened)
                model.input("owner", {"Crouch", "Melee"})
                self.assertEqual(owner["MenuOpen"], not opened)
                self.assertTrue(owner["MeleeConsumed"])
                owner["melee"] = True
                model.globals["ActivePlayer"] = "owner"
                model.run("ProcessSuperPunch")
                self.assertEqual(model.kills, [("target", "owner")])
                target["alive"] = True
                model.run("ProcessSuperPunch")
                model.fire("89i1", "owner", victim="target")
                model.run("ProcessGlobalEventQueue")
                self.assertEqual(model.kills, [("target", "owner")])

    def test_native_hit_queued_before_or_after_combo_still_kills_once(self):
        for queued_before in (False, True):
            for opened in (False, True):
                with self.subTest(queued_before=queued_before, opened=opened):
                    model, owner, target = self.punch_lobby(opened=opened)
                    if queued_before:
                        self.assertTrue(model.fire("89i1", "owner", victim="target"))
                    model.input("owner", {"Crouch", "Melee"})
                    if not queued_before:
                        self.assertTrue(model.fire("89i1", "owner", victim="target"))
                    self.assertEqual(owner["MenuOpen"], not opened)
                    self.assertTrue(owner["MeleeConsumed"])
                    model.run("ProcessGlobalEventQueue")
                    self.assertEqual(model.kills, [("target", "owner")])
                    target["alive"] = True
                    model.fire("89i1", "owner", victim="target")
                    model.run("ProcessGlobalEventQueue")
                    self.assertEqual(model.kills, [("target", "owner")])

    def test_combo_does_not_bypass_protection_or_rearm_a_protected_contact(self):
        for native in (False, True):
            with self.subTest(native=native):
                model, owner, target = self.punch_lobby(protected=True)
                model.input("owner", {"Crouch", "Melee"})
                if native:
                    model.fire("89i1", "owner", victim="target")
                    model.run("ProcessGlobalEventQueue")
                else:
                    owner["melee"] = True
                    model.globals["ActivePlayer"] = "owner"
                    model.run("ProcessSuperPunch")
                self.assertEqual(model.kills, [])
                target.update(UnkillableActive=False, UnkillableMode=0)
                model.fire("89i1", "owner", victim="target")
                model.run("ProcessGlobalEventQueue")
                self.assertEqual(model.kills, [])


if __name__ == "__main__":
    unittest.main()
