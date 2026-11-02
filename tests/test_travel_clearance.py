"""Execute the Travel solver with controlled walkable positions and ray hits.

These tests cover clearance decisions, not native map geometry or hero capsules.
"""
import re
import unittest

from tests.test_camera_reinitialization import CameraResetEvaluator, PATHS
from tests.test_fly_motion import Vector
from tools import validate_workshop as semantic


ZERO = Vector(0, 0, 0)
POINT = Vector(10, 2, 10)
DIRECTIONS = ("east", "west", "north", "south")


class ClearanceEvaluator(CameraResetEvaluator):
    def __init__(self, text, walls=None, ceiling=10, ground=True, route_clear=True):
        super().__init__(text)
        self.walls = walls or {}
        self.ceiling = ceiling
        self.ground = ground
        self.route_clear = route_clear
        self.rays = []
        self.add("owner", TravelDestination=POINT + Vector(2, 0, 0))
        self.globals["TriggerPlayer"] = "owner"

    def call(self, name, args):
        if name == "NearestWalkablePosition":
            # A narrow ledge can project a proposed wall correction back to
            # the same candidate. Final clearance must still reject it.
            return POINT
        if name == "RayCastHitPosition":
            start, end, include, exclude, owned = args
            assert (include, exclude, owned) == ([], [], False)
            self.rays.append((start, end))
            delta = end - start
            if delta.y < 0:
                return POINT if self.ground else end
            if delta.y > 0:
                height = max(0, min(delta.y, POINT.y + self.ceiling - start.y))
                return start + Vector(0, height, 0)
            if start == POINT + Vector(0, 1, 0):
                direction = ("east" if delta.x > 0 else "west" if delta.x < 0
                             else "north" if delta.z > 0 else "south")
                distance = min(delta.magnitude(), self.walls.get(direction, float("inf")))
                return start + delta.normalized() * distance
            return end if self.route_clear else start
        return super().call(name, args)

    def solve(self):
        # Expand native += for the shared interpreter's assignment grammar.
        body = re.sub(r"(Global\.TriggerPlayer\.SafeRevivePosition)\s*\+=\s*([^;]+);",
                      r"\1 = \1 + \2;", self.body("FindSafeTravelPosition"))
        self.execute(body)
        return self.players["owner"]["SafeRevivePosition"]


class TravelClearanceTests(unittest.TestCase):
    def test_each_horizontal_direction_rejects_obstructions_below_final_clearance(self):
        for path in PATHS:
            text = path.read_text(encoding="utf-8")
            for direction in DIRECTIONS:
                for distance in (0, 0.5, 0.849, 0.85, 0.999, 1, 1.249):
                    with self.subTest(artifact=path.name, direction=direction, distance=distance):
                        self.assertEqual(ClearanceEvaluator(text, {direction: distance}).solve(), ZERO)

    def test_exact_clearance_and_no_hit_remain_usable_without_short_duplicate_rays(self):
        for path in PATHS:
            text = path.read_text(encoding="utf-8")
            for distance in (1.25, 1.499, 1.5, 10, float("inf")):
                model = ClearanceEvaluator(text, dict.fromkeys(DIRECTIONS, distance))
                with self.subTest(artifact=path.name, distance=distance):
                    self.assertEqual(model.solve(), POINT + Vector(0, 0.5, 0))
                    self.assertEqual(len(model.rays), 12)
                    horizontal = [(start, end) for start, end in model.rays
                                  if start == POINT + Vector(0, 1, 0)]
                    self.assertEqual(len(horizontal), 8)
                    self.assertTrue(all((end - start).magnitude() == 1.5
                                        for start, end in horizontal))

    def test_head_ground_and_route_guards_still_reject_invalid_destinations(self):
        for path in PATHS:
            text = path.read_text(encoding="utf-8")
            for changes in ({"ceiling": 2}, {"ceiling": 2.49},
                            {"ground": False}, {"route_clear": False}):
                with self.subTest(artifact=path.name, changes=changes):
                    self.assertEqual(ClearanceEvaluator(text, **changes).solve(), ZERO)
            model = ClearanceEvaluator(text, ceiling=2.5)
            self.assertEqual(model.solve(), POINT + Vector(0, 0.5, 0))

    def test_zero_and_distant_destinations_are_rejected(self):
        for path in PATHS:
            for destination in (ZERO, POINT + Vector(9, 0, 0)):
                model = ClearanceEvaluator(path.read_text(encoding="utf-8"))
                model.players["owner"]["TravelDestination"] = destination
                with self.subTest(artifact=path.name, destination=destination):
                    self.assertEqual(model.solve(), ZERO)

    def test_validator_requires_each_final_horizontal_rejection(self):
        text = PATHS[0].read_text(encoding="utf-8")
        rule = semantic.rule_by_subroutine(semantic.extract_rules(text), "FindSafeTravelPosition")
        for vector in ("1.500, 1.000, 0", "-1.500, 1.000, 0",
                       "0, 1.000, 1.500", "0, 1.000, -1.500"):
            weakened = rule.body.replace("Vector(" + vector + ")", "Vector(0, 1.000, 0)")
            mutated = text[:rule.start] + weakened + text[rule.end:]
            checks = semantic.Checks()
            semantic.validate_modes_and_camera(checks, mutated, semantic.extract_rules(mutated))
            with self.subTest(vector=vector):
                self.assertTrue(any("clearance orizzontale finale" in error for error in checks.errors))


if __name__ == "__main__":
    unittest.main()
