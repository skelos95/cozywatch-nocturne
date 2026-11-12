# Cozywatch — Nocturne

Modalità sociale per **Overwatch: Schermaglia, 6v6, fino a 12 giocatori contemporanei**. Personalizza il tuo stile, incontra altre anime e gioca con Camera, Travel, Ghost/Fly, Fates e Dark Roulette.

Il tema **Nocturne** unisce romanticismo oscuro e melodic death metal: argento lunare, malva, rose appassite, cappelle ed echi. I testi nel gioco sono brevi e in inglese; la documentazione è in italiano.

**[Codice da importare](workshop/ruang_irama.en-US.workshop)** · [Importazione](docs/IMPORTAZIONE.md) · [Manuale completo](docs/MANUALE.md)

## Avvio rapido

1. Salva il preset della lobby e imposta la lingua testo del client su **English**.
2. Apri il [file Workshop](workshop/ruang_irama.en-US.workshop), scegli **Raw** e copia tutto in **Custom Game → Settings → Workshop → Paste Rules**.
3. Configura **Skirmish**, fino a 6 slot per squadra e le mappe standard desiderate, escluse quelle Workshop. Il file contiene le regole, non il preset delle mappe.
4. Scegli la durata nelle impostazioni Workshop: **30–60 minuti**, default **30**. Allo zero la partita si riavvia.
5. Al primo spawn trovi **Rites / Controls**: tieni Crouch e premi Interact per aprire la guida completa.

## Comandi

| Azione | Comando |
|---|---|
| Apri/chiudi Nocturne | Tieni premuti insieme Crouch e Melee per 0,5 s da vivo, anche da Travel |
| Scorri un elenco | Crouch + Primary / Secondary |
| Apri, applica o alterna ON/OFF | Crouch + Interact |
| Torna al principale da un sottomenu | Crouch + Reload |
| Ripristina la pagina, dove indicato | Crouch + Ultimate |
| Alterna Camera | Tieni Interact per 0,5 s con Crouch rilasciato |
| Apri Travel & Attach | Tieni Crouch con Nocturne chiuso e Travel ON |
| Resuscita | Jump da morto |

Quando Nocturne è chiuso, il promemoria in alto al centro mostra i tasti per aprirlo e la durata della pressione. Con Travel attivo e Crouch rilasciato, un secondo promemoria mostra il comando Travel sotto il primo, con una riga vuota di separazione.

I comandi usano i tuoi binding. Se rilasci Crouch o Melee prima di 0,5 s, annulli il comando Nocturne. Dopo l'apertura o la chiusura, rilascia Melee prima di ripetere il comando. Rilascia Interact prima di passare dal menu alla Camera. Melee e Death Punch funzionano anche con Crouch tenuto. Con Death Punch attivo, l'impatto può mandare KO un bersaglio valido indipendentemente dal comando Nocturne. Da morto il menu rimane visibile ma non accetta comandi. [Comandi completi e contesti](docs/MANUALE.md#comandi).

## Menu personali

| Pagina | Menu | Funzione |
|---:|---|---|
| 0 | Rites / Controls | Guida ai comandi |
| 1 | Moonlit Name Color | [40 colori Nocturne](docs/NAME_COLORS.md) |
| 2 | Spectral Camera | OFF, il tuo eroe o un bersaglio valido |
| 3 | Soul Soundtrack | [200 generi](docs/GENERI.md), preferenza testuale senza audio |
| 4 | Blood Debt / Revenge | Rivincita per le uccisioni dirette |
| 5 | Deathless | OFF, 1 HP curabile o FULL HP |
| 6 | Echo Voice | 5 preset |
| 7 | Soul Sigil / Icon | Nessuna o 36 icone; FLOATING ON/OFF |
| 8 | Veil Travel / Self Kill | Teletrasporto, Attach e autoeliminazione |
| 9 | Privacy Veil | Blocca le interazioni personalizzate verso di te |
| 10 | Dark Roulette | Sei effetti casuali temporanei |
| 11 | Crown / Vote | Vota un umano, incluso te stesso |
| 12 | Dummy Gaze | Consenti al dummy nemico fermo di guardarti |
| 13 | Ghost / Fly | Attraversa le pareti o vola; toggle indipendenti |
| 14 | Spectral Multijump | Salti aggiuntivi, forza 100–1000% |
| 15 | Death Punch | KO melee ravvicinato, rispettando Unkillable |
| 16 | Speed / Gravity | Velocità 20–1000%, gravità 0–500% |
| 17 | Soul Presence | Stato manuale in Souls & Echoes |
| 18 | Fates | Moneta, dadi e presagi privati |
| 19 | Whispers | Cinque messaggi predefiniti a chi stai mirando |
| 20 | Moonlit Aura | Tre aure personali e filtro delle aure altrui |

Le voci **8, 9, 12 e 15** si alternano direttamente dal principale. Il reset **Crouch + Ultimate** riguarda soltanto la pagina selezionata e compare dove disponibile; conserva i cooldown di Fates e Whispers. [Default e reset](docs/MANUALE.md#ripristino-della-pagina).

Le preferenze restano dopo morte e cambio eroe. **Cambio squadra e uscita/rientro ripristinano i default** e riaprono Rites / Controls. Gli slot lasciati liberi vengono riutilizzati: il limite di 12 riguarda i presenti, non gli ingressi totali.

Privacy blocca Camera, inspection, Teleport, Attach e Whispers verso di te e mostra l'icona fluttuante soltanto a te. FLOATING OFF nasconde l'icona nel mondo a tutti; il simbolo nel roster resta pubblico. Vision di Dark Roulette include intenzionalmente i giocatori privati. La visuale spettatore e gli strumenti nativi restano gestiti dal gioco.

## Stato attuale

[VERSION](VERSION) è **0.8.5**. Include il promemoria dei comandi Nocturne e Travel e la pressione di 0,5 s di Crouch + Melee per aprire o chiudere Nocturne. [Changelog](CHANGELOG.md).

I controlli automatici verificano struttura, regressioni e budget del runtime globale. Importazione, leggibilità, fisica e carico richiedono una prova nel client sul **commit esatto**: i [riscontri disponibili](docs/TEST.md#riscontri-disponibili) distinguono quanto già provato dalle modifiche successive. Conteggi e limiti sono raccolti in [Validazione](docs/VALIDAZIONE.md).

## Documentazione

| Documento | Contenuto |
|---|---|
| [Importazione](docs/IMPORTAZIONE.md) | Copia/incolla e problemi dell'editor |
| [Manuale](docs/MANUALE.md) | Tutti i comandi, default, menu e interazioni |
| [Architettura](docs/PROGETTO.md) | Scheduler, risorse e lifecycle |
| [Validazione](docs/VALIDAZIONE.md) | Controlli automatici, metriche e limiti |
| [Test nel gioco](docs/TEST.md) | Matrice di prova e riscontri storici |
| [Generi](docs/GENERI.md) · [Name Color](docs/NAME_COLORS.md) | Cataloghi musicali e palette |
| [Changelog](CHANGELOG.md) | Storia delle modifiche |

Per modificare il codice parti da [source/](source/README.md), poi rigenera il file importabile ed esegui i controlli documentati.
