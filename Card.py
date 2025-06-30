# Card Class / # Classe Carta
# Rank (integer 1 => 13), Str_Rank (for output), Visible (face down/hidden in current game state) / Rank (intero 1 => 13), Str_Rank (per output), Visibile (coperta/nascosta nello stato attuale del gioco)
class Card:
    def __init__(self, param_rank, suit):
        self.rank = param_rank
        self.str_rank = ['A  ', '2  ', '3  ', '4  ', '5  ', '6  ', '7  ', '8  ', '9  ', '10 ', 'J  ', 'Q  ', 'K  ']
        self.suit = suit
        self.visible = False
        

    # print(card_obj) => calls this method / stampa l'oggetto carta
    # takes into account whether card is currently visible for output / prende in considerazione se la carta è attualmente visibile per l'output
    def __str__(self):
        if self.visible:
            suits_symbols = {
            'hearts': '♥',
            'diamonds': '♦',
            'spades': '♠',
            'clubs': '♣'
            }

            RED = '\033[31m'
            RESET = '\033[0m'
            # Get the symbol for the suit, default to '?' if not found / Prendi il simbolo della seme, predefinito a '?' se non trovato
            symbol = suits_symbols.get(self.suit, '?')
            rank_str = self.str_rank[self.rank - 1].strip()

            if self.suit in ('hearts', 'diamonds'):
                # red suits / semi rossi
                return f"{RED}{rank_str}{symbol}{RESET}"
            else:
                # black suits / semi neri // default
                return f"{rank_str}{symbol}"
        else:
            return '-  '
    
    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True


    