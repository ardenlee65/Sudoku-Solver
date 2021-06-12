class Board:
    def __init__(self, inputBoard):
        self.board = inputBoard

    def __str__(self):
        # call print function
        self.printBoard()
        return ""

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
        print()

    def find_empty(self):
        rows = len(self.board)
        for row in range(rows):
            for col in range(rows):
                if (self.board[row][col] == 0):
                    return (row, col)
        
        # Empty space cannot be found
        return ()

    def valid(self, num, x, y):
        # num is the number we are trying, x is row, y is col
        # need to check vertical, horizontal, and in the 3x3 square

        bound = len(self.board)

        # horizontal
        for row in range(bound):
            if (self.board[row][y] == num) and (row != x):
                return False

        # vertical
        for col in range(bound):
            if (self.board[x][col] == num) and (col != y):
                return False

        # 3x3
        startRow = (x // 3)*3
        startCol = (y // 3)*3
        for row in range(3):
            for col in range(3):
                if (self.board[startRow + row][startCol + col] == num) and ((startRow + row) != x) and ((startCol + col) != y):
                    return False

        return True

    def solve(self):
        moves = self.find_empty()

        # If no more moves, means we filled up the board legally
        if not moves:
            return True
        else:
            row, col = moves

        # Try every valid num
        for attempt in range(1, 10):
            if self.valid(attempt, row, col):
                self.board[row][col] = attempt

                if self.solve():
                    return True

                # If we get here, it means the number we chose did not work
                self.board[row][col] = 0

        return False


if __name__ == "__main__":
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
    game.solve()
    game.printBoard()
