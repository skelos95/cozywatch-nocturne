# Importare il Workshop

## Procedura

1. Salva il preset della lobby e imposta la lingua testo di Overwatch su **English**.
2. Scegli la revisione da importare: il [codice corrente](../workshop/ruang_irama.en-US.workshop) corrisponde alla versione **0.8.4**; la [release v0.8.3](https://github.com/skelos95/cozywatch-nocturne/releases/tag/v0.8.3) conserva il proprio pacchetto storico. Usa il commit per identificare esattamente una prova.
3. Apri il file `.workshop`, scegli **Raw** e copia tutto, da `variables` alla graffa finale, senza numeri di riga o testo della pagina GitHub.
4. In **Custom Game → Settings → Workshop**, usa **Paste Rules**.
5. Apri **Script Diagnostics** e annota **Element Count** e **Largest Rule**, insieme al commit importato.
6. Configura **Skirmish**, fino a 6 slot per squadra e le mappe standard desiderate, escluse quelle Workshop. Scegli la durata **30–60 minuti**, default **30**.
7. Avvia una nuova lobby. Al primo spawn il principale si apre su **Rites / Controls**; **Crouch + Interact** mostra la guida completa.

Il file contiene le regole, non il preset delle mappe. Grammatica, identificatori e interfaccia sono in inglese: non tradurre le keyword. Importa soltanto `workshop/ruang_irama.en-US.workshop`; `source/` e `tests/fixtures/` contengono specifiche e riferimenti interni.

Per comandi, reset, Privacy e interazioni tra funzioni consulta il [manuale](MANUALE.md). Dopo l'importazione verifica la [matrice nel client](TEST.md#regressioni-da-provare), in particolare i cambi successivi all'ultima revisione provata.

## Se l'importazione fallisce

| Sintomo | Verifica |
|---|---|
| Pulsante Paste Rules assente | Il testo completo deve iniziare con `variables`; ricopia dalla vista Raw. |
| Errore con numero di riga | Conserva testo esatto, screenshot e commit; controlla di non avere incluso numeri di riga o delimitatori Markdown. |
| Categorie, impostazioni o testi HUD vuoti | Salva il preset, chiudi e riapri completamente il gioco, poi reimporta. Se persiste, esporta con **Copy Settings** e confronta i testi con il sorgente. |
| Regola troppo lunga o limite elementi | Registra le metriche compilate del client e il messaggio completo. |

Il riavvio completo ha risolto un caso di testi vuoti il 27 settembre 2026; creare una nuova lobby non era bastato. È un rimedio osservato, non una spiegazione della causa interna.

Dalla radice del repository puoi eseguire il preflight locale:

```text
python tools/check_clipboard_import.py workshop/ruang_irama.en-US.workshop --language en-US
```

Controlla UTF-8, stringhe, delimitatori, token strutturali e budget stimati. La compilazione effettiva, Element Count e Largest Rule vanno misurati nel client: [metriche e rapporto](TEST.md#metriche-e-rapporto).

[Torna alla guida](../README.md) · [Controlli completi](VALIDAZIONE.md)
