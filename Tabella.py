# Import Dependencies / Importa le dipendenze
from Card_Stack import Card_Stack

def is_red(card):
    return card.suit in ('hearts', 'diamonds')

def alternate_color(card1, card2):
    return is_red(card1) != is_red(card2)

# Tabella Class / Classe Tabella
class Tabella(Card_Stack):
    def __init__(self):
        Card_Stack.__init__(self)

    # returns boolean: valid to add given cards? / restituisce booleano: valido aggiungere le carte date?
    # (1) cards are visible / (1) le carte sono visibili
    # (2) cards have decreasing rank (1 by 1) / (2) le carte hanno rango decrescente (1 per 1)
    # (3) first new card 1 less than current bottom of Tabella / (3) la prima nuova carta è 1 in meno rispetto al fondo attuale della Tabella
    # (4) colors must alternate / (4) i colori devono alternarsi

    def valid(self, new):

        if not self.top():
            return new[0].visible and new[0].rank == 13

        top_card = self.top()

        for i, c in enumerate(new):
            if not c.visible:
                return False

            if i == 0:
                if not (alternate_color(c, top_card) and c.rank == top_card.rank - 1):
                    return False
            else:
                prev = new[i - 1]
                if not (alternate_color(c, prev) and c.rank == prev.rank - 1):
                    return False

        return True

    # Assumes valid is called first / Presuppone che valido sia chiamato per primo
    def add(self, new):
        for c in new:
            self.cards.append(c)

    # Get copy of cards from index i onwards / prendi una copia delle carte dall'indice i in poi
    def view_cards(self, i):
        # check valid index / controlla l'indice valido
        if (i >= 0) and (i < len(self)):
            return self.cards[i:]
        else:
            return []

    # Remove cards from index i onwards / Rimuovi le carte dall'indice i in poi
    # Can only remove visible cards! / Puoi rimuovere solo le carte visibili!
    def remove_cards(self, i):
        # check valid index / controlla l'indice valido
        if (i >= 0) and (i < len(self)):
            for c in range(i, len(self)):
                if not self.cards[c].visible:
                    return []

            # visible cards => remove! // carte visibili => rimuovi!
            answer = self.cards[i:]             # save cards being moved / salva le carte mosse
            self.cards = self.cards[:i]         # modify this Tabella / modifica questa Tabella

            # make top card visible in new resulting Tabella / rendi visibile la carta superiore nella nuova Tabella risultante
            if not self.empty():
                self.top().show()

            return answer
        else:
            return []

    # returns whether index == next spot in Tabella / restituisce se l'indice == il prossimo posto nella Tabella
    def next_spot(self, i):
        return (i == len(self))

    # returns whether index == last/bottom element in Tabella / restituisce se l'indice == l'ultimo elemento in basso nella Tabella
    def last_spot(self, i):
        return (i == len(self)-1)

    # get "print string" of an element in Tabella / ottieni "stringa di stampa" di un elemento nella Tabella
    def get_str(self, i):
        if i < len(self.cards):
            return str(self.cards[i])
        else:
            return '   '
