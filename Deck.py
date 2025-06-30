# Import Dependencies / Importa le dipendenze
from Card_Stack import Card_Stack
from Card import Card
from random import randint

# Deck Class / # Classe Mazzo
class Deck(Card_Stack):
    def __init__(self):
        Card_Stack.__init__(self)

        # create 52 cards (4/rank) and add to Deck
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        for suit in suits:
            for r in range(1, 14):
                c = Card(r, suit)
                self.cards.append(c)

        self.shuffle()
        self.pointer = 0
        self.discarded = []  # cards discarded (played from deck) / carte scartate (giocate dal mazzo)

        # pointer = index to only 1 "viewable" card in deck during game / pointer = indice per l'unica carta "visibile" nel mazzo durante il gioco
        self.pointer = 0

    # Shuffle Deck / Mischia il mazzo
    def shuffle(self):
        # starting from last element, randomly swap 1 by 1 / iniziare dall'ultimo elemento, scambiare casualmente 1 alla volta
        # first element will be swapped by default / il primo elemento sarà scambiato per impostazione predefinita
        for i in range(len(self.cards)-1, 0, -1):
            # pick a random index from 0 to i / scegliere un indice casuale da 0 a i
            j = randint(0, i)

            # swap arr[i] with arr[j] / scambia arr[i] con arr[j]
            self.cards[i],self.cards[j] = self.cards[j],self.cards[i]

    # Note: No add function -- can't add elements to deck (only remove, 1 at a time) / Note: Nessuna funzione di aggiunta -- non è possibile aggiungere elementi al mazzo (solo rimuovere, 1 alla volta)

    # Current "viewable" element in Deck / Elemento "visibile" corrente nel mazzo
    def top(self):
        return self.cards[self.pointer]

    # Increment pointer: need new viewable card / Incrementa il puntatore: è necessaria una nuova carta visibile
    def increment(self):
        if not self.cards:
            print("♻️ Mazzo vuoto. Rimescolo le carte scartate...")
            self.rebuild_deck()

        # hide old card / nascondi la vecchia carta
        self.cards[self.pointer].hide()

        self.pointer += 1
        if (self.pointer >= len(self)):
            self.pointer = 0

        # show new card / mostra la nuova carta
        self.cards[self.pointer].show()

    # Rebuild deck from discarded cards / Ricostruisci il mazzo dalle carte scartate
    def rebuild_deck(self):
        if not self.discarded:
            print("❌ Nessuna carta da rimescolare.")
            return

        self.cards = self.discarded
        self.discarded = []
        self.shuffle()
        self.pointer = 0
        self.cards[self.pointer].show()

    # Remove "viewable" element from deck / Rimuovi l'elemento "visibile" dal mazzo
    def pop(self):
        if not self.cards:
            print("♻️ Mazzo vuoto. Rimescolo le carte scartate...")
            self.rebuild_deck()

        answer = self.cards[self.pointer]

        self.discarded.append(answer)

        # Delete from deck array, make new "top" visible / Elimina dall'array del mazzo, rendi visibile il nuovo "top"
        # Note that self.pointer index doesn't change / Nota che l'indice self.pointer non cambia
        del self.cards[self.pointer]
        self.cards[self.pointer].show()

        return answer
