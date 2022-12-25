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
            print("\n|---+---+---|")   

    def isMarked(self, row, col):
        if self.gameBoard[int(row)-1][int(col)-1] == '_':
            return False
        else:
            return True


    def tick_Box(self, current_mark):
        row, col = input("Enter the row and column you wish to mark: ").split()
        while True:
            if self.isMarked(row, col) == True:
                row, col = input("Oops already marked, try again: ").split()
            else:
                self.gameBoard[int(row)-1][int(col)-1] = current_mark
                return        

    def check_win(self, current_mark):
        bdlen = len(self.gameBoard)
        
     

    def check_full(self):
        for row in self.gameBoard:
            for mark in row:
                if mark == '_':
                    return False
        return True

    def flip(self, current_mark):
        if current_mark == 'X':
            return 'O'
        else:
            return 'X'

    def play_game(self):
        self.makeBoard()
        P1_mark, P2_mark = self.XsorOs()
        print(f"Player 1 is {P1_mark} \nPlayer 2 is {P2_mark}")
        current_mark = P1_mark
        while True: # Game Loop
            print(f"Current Player's Mark: {current_mark}")
            
            self.print_bd()

            self.tick_Box(current_mark)

            if self.check_win(current_mark):
                print(f"Congratulations! {current_mark} has won!")
                break

            if self.check_full():
                print("No winners. Board full")
                break
            
            current_mark = self.flip(current_mark)


game = Tictactoe()
game.play_game()
