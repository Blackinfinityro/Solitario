# Card Stack: Abstract Class / Stack di carte: classe astratta
# Framework for Tabella, Foundations, and Deck / Framework per Tabella, Finale e Mazzo
class Card_Stack:
    def __init__(self):
        self.cards = []

    # len(card_stack_obj) => calls this method / len(card_stack_obj) => chiama questo metodo
    def __len__(self):
        return len(self.cards)

    def top(self):
        if not self.empty():
            return self.cards[-1]
        else:
            return None

    def empty(self):
        return len(self) == 0
