

class Board:
    game = [[0 for i in range(3)] for j in range(3)]

    def __init__(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j] = 0

    # to print what slots are available in the board
    def printBoard(self):
        count = 0
        for i in range(3):
            for j in range(3):
                value = self.game[i][j]
                if value == 0:
                    print(count, " ", end="")
                elif value == 1:
                    print("O  ", end="")
                elif value == 2:
                    print("X  ", end="")
                else:
                    print("err",value, end="")
                count += 1
            print("")
            print("")  # as an endline

    # for user input in the board, returns true if successful and returns false if unsuccessful
    def add(self, side, input):
        
        if '/q' in input:
            if side == 1:
                print("Client has surrendered")
            elif side == 2:
                print("Server has surrendered")
            return True
        try: # in case input can't be converted to int
            place = int(input)
            i = int(place/3)
            j = place%3
            # invalid spot
            if self.game[i][j] == 1 or self.game[i][j] == 2:
                print("Please choose an available spot")
                return False
            elif side == 1 or side == 2:
                self.game[i][j] = side
                return True
            #invalid input, shouldn't happen
            else:
                print("Please choose a valid input")
                return False
        except ValueError :
            print("Please choose a valid input")
            return False

    def checkWinner(self):  # returns true if game has ended, false if it has not, and prints winner message if true
        result = False

        # straight lines
        for i in range(3):
            if self.game[i][1] == self.game[i][0] and self.game[i][1] == self.game[i][2]:
                if self.game[i][1] == 1:
                    print("Client wins!")
                    result = True
                elif self.game[i][1] == 2:
                    print("Server wins!")
                    result = True
            elif self.game[1][i] == self.game[0][i] and self.game[1][i] == self.game[2][i]:
                if self.game[1][i] == 1:
                    print("Client wins!")
                    result = True
                elif self.game[1][i] == 2:
                    print("Server wins!")
                    result = True

        # diagonal
        if self.game[1][1] == self.game[0][0] and self.game[1][1] == self.game[2][2]:
            if self.game[1][1] == 1:
                print("Client wins!")
                result = True
            elif self.game[1][1] == 2:
                print("Server wins!")
                result = True
        elif self.game[0][2] == self.game[1][1] and self.game[0][2] == self.game[2][0]:
            if self.game[1][1] == 1:
                print("Client wins!")
                result = True
            elif self.game[1][1] == 2:
                print("Server wins!")
                result = True

        # no winner, don't check if there already is a winner
        if result == False:
            flag = True
            for i in range(3):
                for j in range(3):
                    if self.game[i][j] == 0:
                        flag = False
                        break

            if flag == True:
                result = True
                print("The board is full, there is no winner")

        return result
