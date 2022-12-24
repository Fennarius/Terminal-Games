import random

class Tictactoe:
    def __init__(self):
        self.gameBoard = [] # A list that acts as the game board

    def makeBoard(self):
        for rows in range(3):
            row = [] # Make an empty row list
            for space in range(3):
                row.append('_') # Put a '_' character in all 3 spaces of the row
            self.gameBoard.append(row) # Put a completed row into the gameBoard

    def XsorOs(self): 
        while True:  # Input Validation Loop
            print("Will Player 1 be X's or O's: ")
            XorO = input()
            XorO.upper()
            if XorO == 'X':
                return 'X', 'O'
            elif XorO == 'O':
                return 'O', 'X'
            else:
                print("That input doesn't look right, please try again")
                continue

    def print_bd(self):
        for row in self.gameBoard:
            x = 0
            for item in row:
                if x == 0:
                    print("|", item, end = " | ")
                else:
                    print(item, end=" | ")
                x += 1
            print("\n|---|---|---|")            

    def play_game(self):
        self.makeBoard()
        P1_mark, P2_mark = self.XsorOs()
        print(f"Player 1 is {P1_mark} \nPlayer 2 is {P2_mark}")
        current_mark = P1_mark
        while True: # Game Loop
            print(f"Current Player's Mark: {current_mark}")
            
            self.print_bd()
            break


game = Tictactoe()
game.play_game()
