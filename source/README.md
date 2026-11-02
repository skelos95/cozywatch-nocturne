# Specifica comportamentale

`ruang_irama.en-US.source` è l'input del compilatore globale. Deve restare equivalente al riferimento `tests/fixtures/semantic_reference.txt`, su cui si applicano i contratti comportamentali.

**Non importare questa specifica nel gioco:** usa il [clipboard generato](../workshop/ruang_irama.en-US.workshop). Il compilatore trasforma le regole per-player in controller atomici, timer e registrazioni di eventi gestiti dallo scheduler globale.

Grammatica Workshop, identificatori, nomi delle regole, commenti e interfaccia sono in inglese. I nomi propri, compreso `งูแรร์`, mantengono i caratteri originali. I testi e i colori seguono il tema **Nocturne**, ispirato al romanticismo oscuro e al melodic death metal.

## Modificare il codice

1. Aggiorna la specifica e il riferimento comportamentale in modo equivalente.
2. Rigenera il clipboard e il riferimento runtime:

   ```text
   python tools/build_global_runtime.py
   ```

3. Verifica che gli output siano aggiornati ed esegui i gate:

   ```text
   python tools/build_global_runtime.py --check
   python tools/validate_workshop.py
   python tools/check_clipboard_import.py workshop/ruang_irama.en-US.workshop --language en-US
   ```

4. Esegui i test pertinenti e la suite completa prima dell'unione, come descritto in [Validazione](../docs/VALIDAZIONE.md).

Gli identificatori delle regole della specifica restano stabili per compilatore e test. I titoli del clipboard vengono invece numerati consecutivamente a partire da 0, senza duplicati o suffissi alfabetici; questo non modifica le subroutine o il comportamento.

La versione corrente è **0.8.4**; le release precedenti conservano i pacchetti storici. Generazione e test offline non sostituiscono la prova nel client sul commit esatto.

[Architettura e contratti](../docs/PROGETTO.md) · [Manuale](../docs/MANUALE.md) · [Test nel gioco](../docs/TEST.md) · [Changelog](../CHANGELOG.md)
