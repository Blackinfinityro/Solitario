# Italiano
# 🃏 Solitario - Progetto in Python

**Solitario** è un classico gioco di carte per un solo giocatore, sviluppato in Python e giocabile interamente da console.

## Obiettivo del gioco

Ordinare tutte le 52 carte in 4 pile finali, una per seme, in ordine crescente: A → 2 → 3 → ... → K.

## Come avviare il progetto

## Requisiti
- Python 3.x installato (consigliato: Python 3.8+)

## Avvio del gioco

1. Clona o scarica il progetto
2. Apri un terminale nella cartella del progetto
3. Avvia con:

```bash
python Solitario.py
```
oppure in VS Code premi esegui nel file Solitario.py

## Comandi di gioco

Ogni mossa si scrive così:

<riga_sorgente> <colonna_sorgente> <riga_destinazione> <colonna_destinazione>

### Esempi:
R0 D0 R1 T4 → prendi la carta visibile dal mazzo e mettila sulla riga 1 della colonna 4.

R3 T1 R0 F2 → prendi dalla riga 3 della colonna 1 e mettila nella pila finale 2.

R0 D0 R0 D0 → pesca una nuova carta dal mazzo.

## Comandi speciali:
restart → Riavvia la partita

exit → Esci dal gioco

## Struttura del progetto

File	Descrizione

Solitario.py Entry point del gioco. Gestisce interazione utente

Game.py	Contiene la logica di gioco principale

Card.py	Definisce l’oggetto Card

Deck.py	Gestisce il mazzo di carte e la pesca

Tabella.py	Gestisce le 7 colonne di gioco

Foundation.py	Gestisce le pile finali (una per seme)

Card_Stack.py	Classe base per pile di carte

## Regole implementate

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

## Dipendenze:
Nessuna dipendenza esterna. Solo Python standard library.

**Rosario Tabone**

# English
# 🃏 Solitaire - Python Project

**Solitaire** is a classic single-player card game, developed in Python and fully playable in the console.

## Game Objective

Arrange all 52 cards into 4 final piles, one for each suit, in ascending order: A → 2 → 3 → ... → K.

## How to Run the Project

### Requirements
Python 3.x installed (recommended: Python 3.8+)
### Starting the Game
1. Clone or download the project
2. Open a terminal in the project folder
3. Run with:
```bash
python Solitario.py
```
Or press run on the file Solitario.py

## Game Commands
Each move is written as follows:

<source_row> <source_column> <destination_row> <destination_column>
### Examples:

R0 D0 R1 T4 → take the visible card from the deck and place it on row 1 of column 4.

R3 T1 R0 F2 → take from row 3 of column 1 and place it in foundation pile 2.

R0 D0 R0 D0 → draw a new card from the deck.

## Special Commands:
restart → Restart the game

exit → Quit the game

## Project Structure
File	Description

Solitario.py	Game entry point. Handles user interaction

Game.py	Contains the main game logic

Card.py	Defines the Card object

Deck.py	Manages the deck and card drawing

Tabella.py	Manages the 7 playing columns

Foundation.py	Manages the foundation piles (one per suit)

Card_Stack.py	Base class for card stacks

## Implemented Rules
✅ 52 cards, 4 suits (♥ ♦ ♣ ♠)

✅ 7 initial columns, with only the last card face up

✅ Draw cards from the deck one at a time

✅ Stack cards in descending order and alternating colors


✅ Only Kings can be placed on empty columns

✅ Automatic reshuffling when the deck is exhausted

✅ Automatic revealing of the card beneath when a column is freed

✅ Clear error messages and validation

## Endgame Conditions
🏆 Win: all cards are correctly ordered in the 4 foundation piles.

🔄 Restart: type restart

❌ Exit: type exit

## Dependencies
No external dependencies. Only Python standard library.

**Rosario Tabone**




