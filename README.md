# 🃏 Solitario - Progetto in Python

**Solitario** è un classico gioco di carte per un solo giocatore, sviluppato in Python e giocabile interamente da console.

## 🎯 Obiettivo del gioco

Ordinare tutte le 52 carte in 4 pile finali (Foundation), una per seme, in ordine crescente: A → 2 → 3 → ... → K.

---

## 🚀 Come avviare il progetto

### Requisiti
- Python 3.x installato (consigliato: Python 3.8+)

### Avvio del gioco

1. Clona o scarica il progetto
2. Apri un terminale nella cartella del progetto
3. Avvia con:

```bash
python Solitario.py 

Comandi di gioco

Ogni mossa si scrive così:

<riga_sorgente> <colonna_sorgente> <riga_destinazione> <colonna_destinazione>

Esempi:
R0 D0 R1 T4 → prendi la carta visibile dal mazzo e mettila sulla riga 1 della colonna 4.
R3 T1 R0 F2 → prendi dalla riga 3 della colonna 1 e mettila nella pila finale 2.
R0 D0 R0 D0 → pesca una nuova carta dal mazzo.
Comandi speciali:
restart → Riavvia la partita
exit → Esci dal gioco

Struttura del progetto

File	Descrizione
Solitario.py Entry point del gioco. Gestisce interazione utente
Game.py	Contiene la logica di gioco principale
Card.py	Definisce l’oggetto Card
Deck.py	Gestisce il mazzo di carte e la pesca
Tabella.py	Gestisce le 7 colonne di gioco
Foundation.py	Gestisce le pile finali (una per seme)
Card_Stack.py	Classe base per pile di carte

Regole implementate

✅ 52 carte, 4 semi (♥ ♦ ♣ ♠)
✅ 7 colonne iniziali, con solo l’ultima carta scoperta
✅ Pesca carte dal mazzo una alla volta
✅ Impila carte in ordine decrescente e colori alterni
✅ Solo i Re possono andare in colonne vuote
✅ Rimescolamento automatico del mazzo esaurito
✅ Rivelazione automatica della carta sotto quando si libera una colonna
✅ Controlli con messaggi di errore chiari
✅ Condizioni di fine partita

🏆 Vittoria: tutte le carte sono ordinate nelle 4 pile finali.
🔄 Ricomincia: digita restart
❌ Uscita: digita esci

Dipendenze:
Nessuna dipendenza esterna. Solo Python standard library.


