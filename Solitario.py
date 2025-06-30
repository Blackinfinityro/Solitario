# Import Dependencies / Importa le dipendenze
from Game import Game

# Play Solitaire! / Gioca a Solitario!
# English Version / Versione Inglese
def eng():
    game = Game()
    print("Welcome to Solitaire: Good Luck!")
    print()
    print("Game Instructions")
    print("Move Command Format: [Source Row] [Source Column] [Destination Row] [Destination Column]")
    print()
    print("Move Types and Examples")
    print("(1) New Deck Card: R0 D0 R0 D0")
    print("(2) Deck to Tableau: R0 D0 R8 T1")
    print("(3) Tableau to Tableau: R7 T1 R7 T2 (supports multiple cards)")
    print("(4) Deck to Foundation: R0 D0 R0 F1")
    print("(5) Tableau to Foundation: R7 T1 R0 F1 (supports 1 card only)")
    print("(6) Quit: quit")
    print()
    print(game)

    while not game.game_over():
        print()
        command = input("What is your move?: ")

        if (command == 'quit'):
            print("See you next time!")
            break

        result = False
        try:
            result = game.move(command)
        except:
            print("Invalid Command")

        if result:
            print(game)

# Italian Version / Versione Italiana
def ita():
    game = Game()
    print("Benvenuto al solitario: Buona fortuna!")
    print()
    print("Instruzioni del gioco")
    print("Formato Comando Movimento: [Riga Sorgente] [Colonna Sorgente] [Riga Destinazione] [Colonna Destinazione]")
    print()
    print("Movimento ed Esempi")
    print("(1) Nuova Carta Mazzo: R0 D0 R0 D0")
    print("(2) Mazzo a Tabella: R0 D0 R8 T1")
    print("(3) Tabella a Tabella: R7 T1 R7 T2 (supporta più carte)")
    print("(4) Mazzo a Finale: R0 D0 R0 F1")
    print("(5) Tabella a Finale: R7 T1 R0 F1 (supporta solo 1 carta)")
    print("(6) Esci: esci")
    print()
    print(game)

    while not game.game_over():
        print()
        command = input("Qual è la tua mossa?: ")

        if (command == 'esci'):
            print("A presto!")
            break

        result = False
        try:
            result = game.move(command)
        except:
            print("Comando non valido")

        if result:
            print(game)

if __name__ == "__main__":
    language = input("Choose language/Scegli la lingua (eng/ita): ").strip().lower()
    if language == 'ita':
        ita()
    elif language == 'eng':
        eng()
