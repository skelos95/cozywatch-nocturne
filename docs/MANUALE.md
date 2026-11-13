# Manuale di Cozywatch — Nocturne

Comandi, menu e interazioni della revisione corrente. Per iniziare usa la [guida di importazione](IMPORTAZIONE.md); per lo stato della versione consulta il [README](../README.md#stato-attuale). I nomi dei comandi corrispondono ai binding personali mostrati nel gioco.

## Comandi

| Contesto | Comando | Azione |
|---|---|---|
| Vivo, anche con Travel aperto | Tieni Crouch e premi Melee | Apre o chiude Nocturne una volta |
| Menu con elenco | Crouch + Primary / Secondary | Voce successiva / precedente |
| Menu aperto | Crouch + Interact | Apre/applica; nel principale alterna ON/OFF per le voci 8, 9, 12 e 15 |
| Sottomenu | Crouch + Reload | Torna al menu principale |
| Voce principale selezionata o relativo sottomenu, dove indicato | Crouch + Ultimate | Ripristina i default della sola pagina |
| Soundtrack | Crouch + Ability 1 / 2 | Salta avanti / indietro di 10 generi |
| Crouch rilasciato | Interact tenuto 0,5 s | Alterna Camera, anche con menu aperto |
| Nocturne chiuso, Travel OFF o pagine Travel Player/Bot / Attach | Crouch tenuto | Inspection: eroe e HP del bersaglio |
| Menu chiuso, Travel ON | Crouch tenuto | Travel & Attach |
| Travel & Attach | Crouch + Primary / Secondary, poi Interact | Cambia pagina, poi esegue |
| Attaccato, menu chiuso | Crouch + Reload | Sgancia |
| Morto | Jump | Resuscita sul posto sicuro o recupera dal vuoto |
| Vivo, Multijump ON | Premi o tieni Jump in aria, anche con menu aperto | Salti aggiuntivi con la forza scelta |
| Vivo, Death Punch ON | Melee, anche con Crouch tenuto e menu aperto | KO ravvicinato, anche sui compagni, rispettando Unkillable |

Dopo l'apertura o la chiusura, rilascia Melee prima di ripetere il comando. Rilascia Interact prima di passare dal menu alla Camera. Melee resta un attacco anche con Crouch tenuto. Con Death Punch attivo, l'impatto può mandare KO un bersaglio valido anche quando la stessa pressione apre o chiude Nocturne. Da morto il menu resta visibile ma non accetta comandi. Con Multijump OFF, Jump resta nativo da vivi.

Rites / Controls mostra i binding personali e resta bianca. Le altre pagine mostrano i comandi contestuali sopra le opzioni. Il titolo `cozywatch.org [countdown]` e HOST sono in alto a destra; il roster è **SOULS & ECHOES** e il leader dei voti **CROWN OF ASH**.

Chi non sceglie un eroe all’ingresso riceve **Shion dopo 60 secondi**, al successivo controllo di un secondo. Poi può cambiarlo liberamente; morti e cambi squadra non riavviano questo timer.

La [tabella dei 21 menu](../README.md#menu-personali) riassume le funzioni disponibili. Soundtrack mostra una preferenza testuale nel roster: non riproduce audio.

I titoli Nocturne usano nomi evocativi per le stesse funzioni: Spectral Camera è la Camera, Blood Debt / Revenge è la rivincita, Deathless è Unkillable, Soul Sigil / Icon sceglie l'icona e Death Punch è il KO melee. Dark Roulette è il nuovo nome di Try Your Luck; Fates conserva i risultati cosmetici privati. La tabella del README riporta tutte le etichette attuali.

## Ripristino della pagina

Il ripristino con **Crouch + Ultimate** agisce sulla voce selezionata nel principale o sul relativo sottomenu e compare nell’aiuto soltanto dove disponibile. Richiede un giocatore vivo e applica una sola azione per pressione: Ultimate va rilasciato prima di un nuovo reset. Non modifica le preferenze degli altri.

| Pagina | Default ripristinati |
|---|---|
| 1 — Name Color | Moon White; Charcoal per il profilo speciale |
| 2 — Camera | OFF |
| 3 — Soundtrack | Nessuna selezione, cursore al primo genere; Draconian bloccato escluso |
| 5 — Unkillable | OFF |
| 6 — Hero Voice | NORMAL |
| 7 — Icon | NONE; Poison 2 per il profilo speciale; FLOATING ON |
| 11 — Vote Player | Annulla soltanto il proprio voto |
| 13 — Ghost / Fly | Entrambi OFF |
| 14 — Multijump | OFF, livello 1 |
| 16 — Speed / Gravity | Entrambi 100%, cursore Speed |
| 17 — Presence | Unspoken |
| 18 — Fates | Prima scelta e risultato temporaneo rimosso; cooldown conservato |
| 19 — Whispers | Ricezione ON, cursore sulla ricezione, anteprima e conferma rimosse; cooldown conservato |
| 20 — Moonlit Aura | Aura OFF, filtro delle aure altrui OFF |

Info, Revenge, Luck e i toggle 8, 9, 12 e 15 non offrono questo reset. Il reset non cambia pagina né chiude il menu.

## Presence, Fates, Whispers e Moonlit Aura

Presence aggiunge uno stato alla propria riga **Souls & Echoes**, senza creare una targhetta sopra al personaggio. `Unspoken` è il default e non aggiunge testo. Tutti gli stati, compreso `Away beyond the veil`, sono scelte manuali: non rilevano automaticamente l'inattività e non modificano movimento, protezioni o Privacy.

**Fates** offre Moon/Ash, d6, d20, una percentuale intera 1–100% o uno dei sei presagi. Il risultato privato appare sotto Nocturne per **3–4 secondi**; il menu indica READY o WAIT. Sono risposte cosmetiche, senza gli effetti fisici di Dark Roulette. Puoi tirare ogni **5 secondi**; il reset rimuove il risultato senza annullare l’attesa.

**Whispers** offre Greeting, Respect, Rose, Embrace e Resonance. Tieni Crouch nella pagina 19 e mira a un altro umano vivo: il nome del destinatario valido compare nel menu. Servono mira entro **12°**, linea di vista libera, Privacy OFF e ricezione ON; **non c’è limite di distanza**. Dummy e AI sono esclusi. Rilasciare Crouch, uscire dalla pagina o morire cancella l’anteprima. L’invio ricontrolla la mira attuale.

Il destinatario riceve il messaggio e il mittente una conferma privata; nel menu compare anche `SENT: <messaggio> -> <nome>` per **3 secondi**. Solo un invio riuscito avvia il cooldown personale di **15 secondi**. Il menu mostra `WAIT Xs` durante l’attesa e `READY` quando puoi inviare di nuovo; il suggerimento per mirare usa il tuo binding Crouch. La ricezione parte da ON e può essere disattivata; il reset la riattiva e pulisce anteprima/conferma senza cancellare il cooldown. Whispers non è una chat libera e non modifica microfono o animazioni.

**Moonlit Aura** offre Moonlit Ring, Withered Halo e Veil of Ash, inizialmente OFF. Hai un solo effetto personale, nel tuo Name Color; **Hide other auras** nasconde le aure altrui soltanto sul tuo schermo. Morte e perdita dello spawn nascondono l’effetto conservando la scelta; alla rinascita torna entro un secondo. Il cambio colore aggiorna l’aura entro lo stesso intervallo. Il reset spegne la tua aura e disattiva il filtro.

## Travel e Camera

Travel contiene cinque pagine: Teleport Spawn, Teleport Objective, Teleport Player/Bot, Attach e Self Elimination. Con Crouch tenuto, Primary/Secondary cambiano pagina e Interact esegue. Premi Melee mentre tieni Crouch per passare subito da Travel a Nocturne. L'aggancio Attach resta attivo. I comandi richiedono un giocatore vivo e spawnato. La morte chiude Travel.

Self Kill ha un cooldown personale di 3 secondi. Se riapri la pagina durante l'attesa, il testo mostra i secondi residui fino a quando il comando torna disponibile. Un tentativo anticipato indica il tempo residuo al momento della pressione.

Un teletrasporto riuscito interrompe Attach e permette a Multijump di riprendere. Una destinazione rifiutata o un comando Spawn senza spostamento conserva invece l’aggancio. Con Nocturne chiuso, **Crouch + Reload** sgancia manualmente.

Nel menu 2 applicare Your Hero o un bersaglio valido riavvia la Camera, anche se la scelta era già attiva. La Camera si riavvia anche dopo un teletrasporto Travel riuscito o il cambio del proprio eroe. Un bersaglio morto, uscito, privato o in transizione viene revocato. Camera OFF la ferma sempre.

## Movimento e combattimento

Il menu 16 modifica due valori personali, inizialmente al **100%**. Tieni Crouch e premi Interact per scegliere Speed o Gravity; Primary / Secondary aumentano o diminuiscono subito il valore: passi di **20 punti percentuali sotto il 100%**, di **100 sopra il 100%**. Il passaggio tra le fasce è `60 ↔ 80 ↔ 100 ↔ 200 ↔ 300`; al 100% Primary sale a 200 e Secondary scende a 80. La velocità va da **20% a 1000%**, la gravità da **0% a 500%**. Reload torna al principale. Crouch + Ultimate ripristina insieme Speed e Gravity al 100% e seleziona Speed. Le scelte restano dopo morte e cambio eroe e tornano al 100% dopo cambio squadra o uscita/rientro.

Ghost attraversa pareti e soffitti mantenendo il pavimento. Applicare o alternare Ghost aggiorna soltanto la collisione con l'ambiente e conserva l'inerzia, anche durante un salto o mentre Fly è attiva. Fly segue lo sguardo con avanti; indietro e laterali restano orizzontali. La velocità è fissa sul valore scelto nel menu 16: **100% equivale a 5,5 m/s**, senza accelerazione automatica. Con Fly attiva la gravità è sempre **0**; disattivandola torna al valore scelto nel menu 16. Luck Acceleration mantiene il suo effetto temporaneo e, alla fine, vengono ripristinate le impostazioni personali.

Multijump aggiunge salti in aria premendo Jump o tenendolo premuto: la ripetizione avviene ogni 0,3 s e il valore scelto resta fisso. Funziona anche con un menu aperto; si sospende con Attach, Fly o Luck Acceleration. La percentuale indica la spinta verticale del salto aggiuntivo, non l'altezza in metri. Ogni salto valido mostra un breve anello RGB arcobaleno sotto i piedi; i comandi dei menu non generano effetti visivi.

Death Punch è inizialmente OFF e funziona anche con il menu principale, un sottomenu o Travel aperto, usando Melee anche con Crouch tenuto. Il KO dipende dal contatto dell'attacco. Se premi Melee con Crouch tenuto, apri o chiudi Nocturne con la stessa pressione. Durante un attacco melee cerca subito un bersaglio vicino davanti, anche della propria squadra, senza attraversare muri. Un impatto melee nativo sui nemici viene riconosciuto anche fra due aggiornamenti dell'animazione. Un solo contatto per attacco, rispettando Unkillable. Revenge registra anche queste uccisioni fra umani alleati. La preferenza si conserva dopo morte o cambio eroe e torna OFF al cambio squadra o all'uscita.

## Tema, colori e icone

La diagnostica server è bianca e visibile soltanto all’host. Menu, HUD e messaggi sono in inglese; il nome personale `งูแรร์` conserva i caratteri originali.

I [40 Name Color](NAME_COLORS.md) seguono le sfumature Nocturne: argento, grigi, nero, ori antichi, terre autunnali, rose appassite, viola, blu lunari e verde muschio. Preview, nome e icona usano il colore esatto scelto, inizialmente Moon White. Info resta bianca; le altre pagine mescolano il colore personale al proprio accento. Titolo, HOST, effetti Luck e anello Multijump conservano il ciclo RGB arcobaleno di 51 secondi.

Le 36 icone fluttuano intorno al proprietario, sempre entro **5 m**, seguendone movimento e teletrasporti. Il menu 7 offre NONE, le icone e infine **FLOATING ON/OFF**: il toggle nasconde o mostra il simbolo nel mondo senza cambiare quello scelto. Il default e il reset sono ON. Con Privacy ON l’icona attiva è visibile soltanto al proprietario; FLOATING OFF la nasconde a tutti. Il simbolo nella lista Souls & Echoes resta sempre pubblico e bianco, mentre il testo usa il Name Color. NONE non mostra un simbolo.

## Privacy e preferenze

Privacy impedisce Camera, inspection, Teleport, Attach e Whispers verso il giocatore e riserva al solo proprietario l’icona fluttuante attiva; l'effetto Vision di Dark Roulette mostra intenzionalmente anche i giocatori privati. Whispers ha inoltre un filtro di ricezione personale indipendente. Preferenze, pagina e cursore persistono tra morte e cambio eroe. **Cambio squadra e uscita/rientro ripartono dai default**, aprendo nuovamente il principale su Rites / Controls al completamento della registrazione.

Privacy riguarda le funzioni personalizzate del Workshop: non limita la visuale spettatore o gli strumenti amministrativi nativi.

## Dummy Target e profilo speciale

I dummy compaiono solo in Schermaglia, al massimo uno per squadra con almeno due slot liberi. Lasciano spazio quando la squadra si riempie. Dopo il teletrasporto iniziale verso un punto sicuro restano fermi, senza inseguire: guardano soltanto il nemico umano vivo più vicino con **Dummy Target ON**. La voce `12 - DUMMY GAZE` mostra `DUMMY GAZE: ON/OFF`; ON richiede un dummy avversario presente, OFF è sempre disponibile. Se il dummy avversario scompare, la preferenza torna OFF entro un secondo e richiede una nuova attivazione. Privacy conserva il proprio significato e non viene modificata da questo consenso. [Dettagli tecnici dei dummy](PROGETTO.md#dummy-e-bot-normali)

Il nome visibile esatto `งูแรร์` riceve i default modificabili Charcoal / Poison 2 e il Vibes fisso `Draconian`. Il riconoscimento avviene per nome, quindi vale anche per un omonimo.

[Torna alla guida](../README.md) · [Test nel gioco](TEST.md) · [Architettura](PROGETTO.md)
