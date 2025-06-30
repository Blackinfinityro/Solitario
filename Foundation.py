# Import Dependencies / Importa le dipendenze
from Card_Stack import Card_Stack

# Foundation Class / Finale
class Foundation(Card_Stack):
    def __init__(self):
        Card_Stack.__init__(self)

    # returns boolean: valid to add given card? / restituisce booleano: valido aggiungere la carta data?
    # (1) card must be visible / (1) la carta deve essere visibile
    # (2) rank must be 1 higher than existing top card / (2) il rango deve essere 1 superiore alla carta superiore esistente
    def valid(self, c):
        threshold = 0
        if self.top():
            threshold = self.top().rank

        return (c.rank == threshold+1)

    # add given card: valid must be called first! / aggiungi la carta data: deve essere chiamato prima valido!
    # only supports adding 1 card at a time / supporta solo l'aggiunta di 1 carta alla volta
    def add(self, c):
        # hide existing top card
        if not self.empty():
            self.cards[-1].hide()
        self.cards.append(c)

    # print(foundation_obj) => calls this method / print(foundation_obj) => chiama questo metodo
    # print top card in tableau / stampa la carta superiore nella tabella
    def __str__(self):
        if self.empty():
            return '-  '
        else:
            return str(self.top())

    # whether foundation contains all cards 1...13 / se la fondazione contiene tutte le carte 1...13
    def full(self):
        # must have 13 cards
        if not (len(self) == 13):
            return False

        # one of each rank, increasing / uno di ogni rank, in aumento
        for i in range(1,14):
            if not (self.cards[i].rank == i):
                return False

        return True
