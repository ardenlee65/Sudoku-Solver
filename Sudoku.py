class Board:
    def __init__(self, inputBoard):
        self.board = inputBoard

    #def __str__(self):
        # call print function

    def printBoard(self):
        rows = len(self.board)
        for col in range(rows):
            if (col != 0) and (col%3 == 0):
                print("---------------------")
            for row in range(rows):
                if (row != 0) and (row%3 == 0):
                    print("|", end=" ")
                print(self.board[col][row], end=" ")

            print()




testBoard = [
            [0,0,0,2,6,0,7,0,1],
            [6,8,0,0,7,0,0,9,0],
            [1,9,0,0,0,4,5,0,0],
            [8,2,0,1,0,0,0,4,0],
            [0,0,4,6,0,2,9,0,0],
            [0,5,0,0,0,3,0,2,8],
            [0,0,9,3,0,0,0,7,4],
            [0,4,0,0,5,0,0,3,6],
            [7,0,3,0,1,8,0,0,0],
            ]

game = Board(testBoard)
game.printBoard()