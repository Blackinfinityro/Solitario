# Import Dependencies / Importa le dipendenze
from Deck import Deck
from Tabella import Tabella
from Foundation import Foundation

# Game Class / Classe del Gioco
class Game:
    # Set Up Game, Distribute Cards / Imposta il Gioco, Distribuisci le Carte
    def __init__(self):
        self.Tabella = []
        self.foundations = []
        self.deck = Deck()

        # Create Tabella (7 Columns) / Crea Tabella (7 Colonne)
        for i in range(0, 7):
            self.Tabella.append(Tabella())

        # Distribute Cards to Tabella / Distribuisci le Carte alla Tabella
        for i in range(7, 0, -1):        # i = number cards to deal / i = numero di carte da distribuire
            for j in range(0, i):
                self.Tabella[j].add([self.deck.pop()])
                self.Tabella[j].top().hide()

        # Make Current Card in Deck Visible / Rendi Visibile la Carta Corrente nel Mazzo
        self.deck.top().show()

        # Make Top Card in Each Tabella Visible / Rendi Visibile la Carta Superiore in Ogni Tabella
        for t in self.Tabella:
            t.top().show()

        # Create Foundations (4 Foundations) / Crea Finali (4 Finali)
        for i in range(0, 4):
            self.foundations.append(Foundation())

    # Game Over if all foundations full / Gioco Finito se tutte i finali sono pieni
    def game_over(self):
        for f in self.foundations:
            if not f.full():
                return False
        return True

    # Input Row Syntax Correct (index checked per individual case) / Input Row Syntax Corretto (indice controllato per caso individuale)
    # check length and whether begins with 'R' / controlla la lunghezza e se inizia con 'R'
    def valid_row(self, str):
        if (len(str) == 2) or (len(str) == 3):
            if (str[0] == 'R'):
                return True

        return False # all other invalid, if this point reached / tutti gli altri non validi, se si raggiunge questo punto

    # Input Column Syntax Correct (index checked per individual case) / Input Column Syntax Corretto (indice controllato per caso individuale)
    def valid_col(self, str):
        return str in ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'F1', 'F2', 'F3', 'F4', 'D0']

    # Valid Index for Tabella / Indice valido per Tabella
    def valid_Tabella(self, i):
        return (i >= 0) and (i < len(self.Tabella))

    # Valid Index for Foundations / Indice valido per le Fondazioni
    def valid_foundation(self, i):
        return (i >= 0) and (i < len(self.foundations))


    # MAIN Move Function!!! / FUNZIONE PRINCIPALE di Spostamento!!!
    # (1) New Deck Card / Nuova Carta dal Mazzo
    # (2) Deck to Tabella / Mazzo alla Tabella
    # (3) Tabella to Tabella / Tabella alla Tabella
    # (4) Deck to Foundation / Mazzo al Finale
    # (5) Tabella to Foundation / Tabella al Finale

    def move(self, command):
        sequence = command.split()

        if (len(sequence) != 4):
            print("Invalid Command: format error")
            return False

        from_row = sequence[0]
        from_col = sequence[1]
        to_row = sequence[2]
        to_col = sequence[3]

        # Check Valid Row/Column Names / Controlla i Nomi delle Righe/Colonne Valide
        if not (self.valid_col(from_col) and self.valid_col(to_col) and self.valid_row(from_row) and self.valid_row(to_row)):
            print("Invalid Command: format error")
            return False

        # Move Type 1: New Deck Card /Mossa 1: Nuova Carta dal Mazzo
        if (from_row == 'R0') and (from_col == 'D0') and (to_row == 'R0') and (to_col == 'D0'):
            self.deck.increment()
            return True

        # Move Type 2: Deck to Tabella / Mossa 2: Mazzo alla Tabella
        if (from_row == 'R0') and (from_col == 'D0') and ('T' == to_col[0]):
            to_row = int(to_row[1:]) - 1
            to_col = int(to_col[1:]) - 1

            # must be valid Tabella / deve essere una Tabella valida
            if not self.valid_Tabella(to_col):
                print("Invalid Command: Tabella column error")
                return False

            # target row must be at the end of destination Tabella / la riga di destinazione deve essere alla fine della Tabella di destinazione
            if not self.Tabella[to_col].next_spot(to_row):
                print("Invalid Command: Tabella row error")
                return False

            # look at card to move; move if valid / guarda la carta da spostare; sposta se valida
            move_card = [self.deck.top()]
            if self.Tabella[to_col].valid(move_card):
                self.Tabella[to_col].add([self.deck.pop()])
                return True
            else:
                print("Invalid Command: can't move selected cards")
                return False

        # Move Type 3: Tabella to Tabella / Mossa 3: Tabella alla Tabella
        if ('T' == from_col[0]) and ('T' == to_col[0]):
            from_col = int(from_col[1:]) - 1
            to_col = int(to_col[1:]) - 1
            from_row = int(from_row[1:]) - 1
            to_row = int(to_row[1:]) - 1

            # must be valid Tabella / deve essere una Tabella valida
            if not self.valid_Tabella(from_col) or not self.valid_Tabella(to_col):
                print("Invalid Command: Tabella column error")
                return False

            # target row must be at the end of destination Tabella / la riga di destinazione deve essere alla fine della Tabella di destinazione
            if not self.Tabella[to_col].next_spot(to_row):
                print("Invalid Command: destination Tabella row error")
                return False

            # source row must be between 0 and num elements in source Tabella / la riga di origine deve essere compresa tra 0 e il numero di elementi nella Tabella di origine
            # source Tabella cannot be empty / la Tabella di origine non può essere vuota
            if (self.Tabella[from_col].empty()) or (from_row < 0) or (from_row >= len(self.Tabella[from_col])):
                print("Invalid Command: source Tabella row error")
                return False

            # look at cards to move; move if valid / guarda le carte da spostare; sposta se valide
            move_cards = self.Tabella[from_col].view_cards(from_row)
            if self.Tabella[to_col].valid(move_cards):
                self.Tabella[to_col].add(self.Tabella[from_col].remove_cards(from_row))
                return True
            else:
                print("Invalid Command: can't move selected cards")
                return False

        # Move Type 4: Deck to Foundation / Mossa 4: Mazzo al Finale
        if (from_row == 'R0') and (from_col == 'D0') and (to_row == 'R0') and ('F' == to_col[0]):
            to_col = int(to_col[1:]) - 1

            # must be valid foundation / deve essere un finale valido
            if not self.valid_foundation(to_col):
                print("Invalid Command: foundation column error")
                return False

            # get threshold: destination foundation's top card rank / prendi il limite: rango della carta superiore del finale di destinazione
            move_card = self.deck.top()
            if (self.foundations[to_col].valid(move_card)):
                self.foundations[to_col].add(self.deck.pop())
                return True
            else:
                print("Invalid Command: can't move selected cards")
                return False

        # Move Type 5: Tabella to Foundation / Mossa 5: Tabella al Finale
        if (from_col[0] == 'T') and (to_row == 'R0') and ('F' == to_col[0]):
            from_col = int(from_col[1:]) - 1
            to_col = int(to_col[1:]) - 1
            from_row = int(from_row[1:]) - 1

            # must be valid Tabella / deve essere una Tabella valida
            if not self.valid_Tabella(from_col):
                print("Invalid Command: source Tabella column error")
                return False

            # source row must be bottom of Tabella / la riga di origine deve essere in fondo alla Tabella
            if not self.Tabella[from_col].last_spot(from_row):
                print("Invalid Command: source Tabella row error")
                return False

            # must be valid foundation / deve essere un finale valido
            if not self.valid_foundation(to_col):
                print("Invalid Command: destination foundation column error")
                return False

            # get threshold: destination foundation's top card rank / prendi il limite: rango della carta superiore del finale di destinazione
            move_card = self.Tabella[from_col].top()
            if (self.foundations[to_col].valid(move_card)):
                move_card = self.Tabella[from_col].remove_cards(from_row)
                move_card = move_card[0]
                self.foundations[to_col].add(move_card)
                return True
            else:
                print("Invalid Command: can't move selected cards")
                return False

    # print(game_obj) => calls this method / print(game_obj) => chiama questo metodo
    # print current game state / stampa lo stato attuale del gioco
    def __str__(self):
        # Header Row = Top Card in Deck / Riga di Intestazione = Carta Superiore nel Mazzo
        spot = '   '

        header = spot + 'D0 ' + spot + spot + 'F1 ' + 'F2 ' + 'F3 ' + 'F4 ' + '\n'

        header_cards = 'R0 ' + str(self.deck.top()) + spot + spot
        for f in self.foundations:
            header_cards += str(f)
        header_cards += '\n' + '\n'

        Tabella_header = spot
        for i in range(0, 7):
            Tabella_header += 'T' + str(i+1) + ' '
        Tabella_header += '\n'

        Tabella_str = ''
        max_len = max([len(i) for i in self.Tabella])
        for r in range(0, max_len+1):
            Tabella_str += 'R' + str(r+1)
            if r < 9:
                Tabella_str += ' '
            for t in self.Tabella:
                Tabella_str += t.get_str(r)
            Tabella_str += '\n'

        return header + header_cards + Tabella_header + Tabella_str
