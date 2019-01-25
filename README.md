# AbortiStats
Small research in Italian about the affirmation that in Italy in the 70s there died each year 20,000 women because of 1,000,000 clandestine abortions.

What follows is in Italian.

## Il motto: 20 mila donne morte ogni anno per 1 milone di aborti clandestini.

Il mantra per far passare la legge 194 sull'aborto è sempre stato: *in Italia ogni anno muoiono 20.000 (venti mila) donne per 1.000.000 (un milione di) aborti clandestini*.

Con il presente voglio mettere alla prova queste statistiche.

## Come sfatare un mito.

In un dibattito si devono sostenere tutte le tesi esposte tramite delle prove.

Vi sono una varietà di classi di prove, dai dati alle statistiche, dai principi primi alle opinioni degli esperti. Vi sono anche modi diversi di argomentare, dai discorsi deduttivi a quelli induttivi, dalle arringhe demagogiche alle metafore sentimentali.

Vi è pure un particolare costrutto che è un artificio letterario che ha lo scopo di autopreservarsi una volta creato: si tratta della *teoria del complotto*. Il suo principio di funzionamento è molto semplice: vi è bisogno di un gruppo, i proponitori della tesi, che si dichiari in minoranza e perseguitato da altri, detti complottisti. Il gruppo dei proponitori espone una tesi che dice voler essere negata dai complottisti. Una volta esposta la tesi del complotto, se vi sono prove a favore, queste corroborano la tesi; se invece le prove sono assenti o palesemente contro la tesi, è perché i complottisti nascondono le prove o inventano delle controprove. Una volta creato questo artificio smantellare la tesi diviene molto arduo. Tuttavia non è mai impossibile.

Negli anni '70 la propaganda per la legalizzazione in Italia dell'aborto era basata quasi esclusivamente su una statistica: "In Italia ogni anno muoiono più di 20 mila donne per via del ricorso all'aborto clandestino. Gli aborti clandestini sono più di 1 milione". Come controbattere questa tesi del complotto? Non vi sono statistiche né sulle donne morte da aborti clandestini (si confondono con il resto delle donne morte ogni anno), né sugli aborti (l'aborto era illegale, perciò non si avevano dati sul numero di aborti clandestini). I *media* dell'epoca non hanno mai adeguatamente risposto a questa tesi. I *media* moderni si spingono oltre: non soltanto ripetono pedissequamente le stesse statistiche anno dopo anno all'anniversario dell'entrata in vigore della legge, e comunque in qualsivoglia dibattito pro o contro l'aborto, ma anche (in tempi recenti) riutilizzano le stesse teorie per avallare velleità contro i medici obiettori di coscienza.

Oltre tutto ciò, come in ogni regime che si rispetti, chiunque è sorpreso a criticare viene bullizzato dagli altri. Che fare per ridare un po' di senno a chi l'ha perduto? Andare sulla luna a ritrovarlo? Invocare il presidio di Sant'Ascanio? 

Per fortuna in tempi moderni esistono anche delle scienze nuove, figlie dell'amplesso fra la statistica e l'informatica: si tratta di *data science* e *machine learning* (o *AI* in senso lato). 

Per dimostrare falsa questa teoria mi sono avvalso quindi della nuova disciplina sulla ricerca dei dati. Come ogni ricerca in *data science*, ogni *fake news* si smaschera tramite il ricorso, appunto, ai **dati**.

## Le Fonti: Wikipedia e Istat

Come ogni progetto di *data science* che si rispetti, bisogna fare una ricognizione di campo, ovvero un *saggio preliminare dei dati*

Son partito da Wikipedia, [articolo sulla 194](https://it.wikipedia.org/wiki/Legge_22_maggio_1978,_n._194) (vedi *sources/citation/legge194_wikipedia.txt*); ho ricavato da lì i dati sull'aborto in Italia (*sources/aborti_italia_dati_per_anno.csv*)

Sempre su Wikipedia, [Articolo sulla demografia d'Italia](https://it.wikipedia.org/wiki/Demografia_d%27Italia) (vedi *sources/citation/demografia.txt*) si trovano vari indici demografici, da cui ho ricavato il file *sources/demografia.csv*

L'Istat fornisce dati sulla mortalità. Consultando le [tavole](http://dati.istat.it/Index.aspx?DataSetCode=DCIS_MORTALITA1) (vedi *sources/citation/istat_tavole_di_mortalità.txt*) ho ottenuto un file excel di sommario (consultabile, *sources/istat_tavole_mortalità_donne_età_fertile_processed.xlsx*; al file originario ho aggiunto una riga "totale" che è la somma delle fascie d'età') e il file sulla mortalità (*sources/istat_tavole_mortalità_donne_età_fertile_not_processed.csv*). 

Un appunto: ho preso i dati dal 1974 (i più vecchi consultabili tramite lo strumento) alla data del 2017 (i più recenti disponibili); ho estrapolato i dati su tutto il territorio nazionale su tutti i decessi femminili in età compresa tra i 15 ed i 54 anni (presumibilmente deve includere con un buon margine l'età fertile, giusto per stare tranquilli).

## Preprocessing e generazione dei grafici

Ho creato uno script di pre-processing, ovvero di "pulizia" dei dati, (*/src/preprocessing.py*) che genera in automatico il file */DATA/unified.csv*.

Un altro script (*/src/chart.py*) crea invece i grafici.

Eseguendoli in serie si ottengono i grafici nella cartella *CHARTS/*

## Risultati

### 1. Aborti

Il primo grafico che consideriamo qui riguarda i dati sugli aborti. 

![Grafico sulgi aborti negli anni, dalla promulgazione della 194 a oggi](CHARTS/aborti.png?raw=true "Grafico sulgi aborti negli anni, dalla promulgazione della 194 a oggi")

Come si può apprezzare nei primissimi anni dalla promulgazione il numero degli aborti è cresciuto, per arrivare ad un picco nel 1982 (4 anni dopo la promulgazione) per poi iniziare a scemare.

Perché dunque questa china discendente? Potrebbe la sua causa essere una maggior consapevolezza sui metodi contraccettivi?

### 2. Nascite e Aborti

In questo secondo grafico correliamo gli aborti con le nascite.

![Grafico della correlazione fra aborti e nascite.](CHARTS/nascite_aborti.png?raw=true "Grafico della correlazione fra aborti e nascite.")

Possiamo apprezzare come (a parte variazioni negli anni 1988-1992 e 2004-2010) la tendenza è generalmente verso la diminuzione delle nascite. La linea rossa tratteggiata è appunto la linea di tendenza dei dati sulle nascite, mentre la linea nera lo è sugli aborti. 

Una nota, per correttezza: la linea di tendenza degli aborti è stata calcolata non considerando gli anni prima del 1982, anni in cui c'è stata una crescita enorme degli aborti. Il motivo è presto detto: i primi anni l'aborto era una novità e c'è voluto tempo magari prima che le donne si sentissero libere di andare ad abortire. Comunque la correlazione è evidente anche senza le linee.

Possibile conclusione? La diminuzione negli aborti negli anni è correlata ad una diminuzione delle gravidanze in generale, quindi, forse, all'aumento dei metodi contraccettivi.

### 3. Nascite, Aborti e Popolazione totale

Questo grafico mette in evidenza come la natalità stia diminuendo a fronte di una popolazione in leggero aumento.

![Grafico della correlazione fra aborti, nascite e popolazione totale.](CHARTS/nascite_aborti_popolazione.png?raw=true "Grafico della correlazione fra aborti, nascite e popolazione totale.")

L'asse delle Y è scalato logaritmicamente, altrimenti i dati su aborto e natalità non si vedrebbero, in quanto molto più piccoli dei numeri della popolazione totale.

### 4. Morti e Aborti

In questo grafico vengono correlate le morti rosa, ovvero di donne in età fertile, agli aborti (dichiarati).

![Grafico della correlazione fra morti rosa ed aborti.](CHARTS/morti_aborti.png?raw=true "Grafico della correlazione fra morti rosa ed aborti.")

Come vediamo ci sono molti più aborti che morti rosa. Il dato dichiarato prima del '78 era 1 milione di aborti a fronte di 200 mila morti rosa, quindi un rapporto di **1 morte di donna ogni 5 aborti**.

Con il prossimo grafico entriamo nel vivo: vedremo come le morti rosa hanno subito un freno dopo l'entrata in vigore della 194, che appunto, serve per evitare che 1 donna su 5 muoia per la pratica di aborti clandestini!

### 5. Morti naturali e da Aborti Clandestini

Ecco qui, il grafico che tutti aspettavamo:

![Grafico che mostra l'andamento delle morti rosa.](CHARTS/morti_da_fake_news.png?raw=true "Grafico che mostra l'andamento delle morti rosa.")

Come possiamo vedere, il trend è in diminuzione, senza nessuna frenata dopo il 1978, e con numeri ben al di sotto delle linea dei 200 mila. **200 MILA DONNE MORTE PER ABORTI CLANDESTINI = FAKE NEWS!**, le morti totali di donne in Italia in età fertile sono state molto al di sotto dei 200 mila! 

### 6. Aborti Reali e Aborti Clandestini

Da ultimo un grafico che mostra l'assurdità del numero di 1 milione di aborti clandestini.

![Grafico che mostra la totale infondatezza delle statistiche sugli aborti clandestini.](CHARTS/total_fake_news.png?raw=true "Grafico che mostra la totale infondatezza delle statistiche sugli aborti clandestini.")

Qui possiamo notare come i dati reali sugli aborti siano di molto al di sotto del milione di aborti: se fosse stata una cifra vera, avremmo dovuto assistere nel 1982, quando finalmente non c'era remora sull'aborto, ad un superamento della soglia del milione di aborti: infatti è presumibile che quando gli aborti erano illegali avessero praticato l'aborto clandestinamente solo una percentuale bassa di donne che con la legalizzazione lo avrebbero praticato.

## Conclusione

Pare ovvio: i dati che hanno spinto la propaganda per far passare la 194 erano tutti delle *fake news*. La teoria complottistica è stata provata falsa dai nudi fatti: non c'è nessun complotto, non vi sono mai stati moltissimi aborti clandestini, né tanto meno morti da aborti clandestini. Infatti la tendenza sulle morti è in generale diminuzione, ma non i è nessun apprezzabile differenza prima e dopo l'entrata in vigore della legge sull'aborto.

Coloro i quali hanno dichiarato e continuano a dichiarare false notizie per promuovere questa legge dovrebbero dare ragione delle loro statistiche e rispondere ai fatti con fatti, non con propaganda e *fake news*.

Spero questo breve excursus sui dati sia stato di vostro gradimento.


