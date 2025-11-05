# xmlfatt2pdf

Script Python per convertire XML di fattura elettronica (formato FPA/SDI) in PDF.

## Descrizione

`xmlfatt2pdf.py` è uno script che consente di prendere un file XML di fattura elettronica nel formato standard italiano (e.g. “FatturaPA” / SDI) e generare un PDF leggibile.
L’obiettivo è semplificare la visualizzazione o la stampa di fatture elettroniche XML, senza dover usare software esterni specifici.

## Caratteristiche

- Parsing dell’XML della fattura elettronica (DTE) per estrarre i dati principali: cedente/prestatore, cessionario/committente, articoli, importi, imposte, ecc.
- Generazione di un documento PDF con layout leggibile.
- Facilità di integrazione in processi di backend o script batch.
- Minimale: poche dipendenze, uso diretto da linea di comando.

## Requisiti

- Python 3.x
- Le librerie Python incluse nel file (o eventuali dipendenze esterne)

  > (Controlla l’inizio del file per vedere quali `import` vengono usati)

- Un file XML di fattura elettronica conforme agli standard italiani (SDI)
- Permessi di scrittura per generare il file PDF di output

## Utilizzo

```bash
python xmlfatt2pdf.py <input_fattura.xml> <output_fattura.pdf>
```

Dove:

- `<input_fattura.xml>` è il percorso del file XML da convertire.
- `<output_fattura.pdf>` è il percorso (e nome) del file PDF generato.

### Esempio

```bash
python xmlfatt2pdf.py fattura_123.xml fattura_123.pdf
```

## Parametri supportati

Al momento lo script accetta due argomenti: input XML e output PDF.
Verifica nel codice se sono presenti opzioni aggiuntive (ad esempio per template, filtri, debug…).

## Come funziona (in breve)

1. Lo script carica il file XML e lo parse in memoria.
2. Estrae i campi principali della fattura (intestazione, dettagli, importi).
3. Genera un layout PDF (usando librerie PDF in Python) con i dati estratti.
4. Salva il PDF al percorso indicato.

## Personalizzazione

- È possibile modificare lo script per **aggiungere** o **rimuovere** campi specifici (ex: codici articolo, sconto, note).
- Il layout del PDF può essere adattato (font, margini, logo aziendale).
- Puoi integrarlo come modulo in un’applicazione più ampia (es. generazione automatica delle fatture, invio mail, archivio).

## Possibili miglioramenti

- Gestione di più formati/firme digitali presenti nell’XML.
- Supporto per allegati nella fattura elettronica (es: documenti correlati).
- Migliore impaginazione del PDF (es: pagination, header/footer, logo).
- Logging più dettagliato, modalità batch per cartelle di fatture.
- Configurazione via file `yaml` o `json` (per layout, percorsi, opzioni).

## Contribuire

Se vuoi contribuire:

1. Fork del repository
2. Crea un branch per la tua feature o fix (`git checkout -b mia-feature`)
3. Fai le modifiche, testa con vari file XML reali
4. Apri una pull request descrivendo i cambiamenti

## Autore e contatti

- Autore originale: Simone Cansella
- Repository: [https://github.com/webagens/xmlfatt2pdf](https://github.com/webagens/xmlfatt2pdf)
- Per segnalare bug o richiedere funzionalità: apri un Issue sul repository
