import pygame

class Board:
    def __init__(self, inputBoard):
        self.board = inputBoard
        pygame.init()
        self.screen = pygame.display.set_mode((460, 600))
        self.icon = pygame.image.load('sudoku-svgrepo-com.svg')
        self.title = pygame.font.SysFont('monospace', 70, bold=True)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Sudoku")
        self.font = pygame.font.SysFont('monospace',30, bold=True)
        start = True
        self.drawWholeBoard()
        # write "press enter to start"

        text = self.font.render("Press \"Enter\" to begin", True, (0,0,0), (224,224,224))
        textRect = text.get_rect()
        textRect.center = ((230,550))
        self.screen.blit(text, textRect)
        pygame.display.update()

        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start = False

        if self.solve():
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()


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
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                self.board[row][col] = attempt

                self.drawWholeBoard()

                pygame.time.delay(150)

                if self.solve():
                    return True

                # If we get here, it means the number we chose did not work
                self.board[row][col] = 0

        return False

    def drawWholeBoard(self):

        self.screen.fill((224,224,224))

        # Draws Sudoku board

        # Outer box
        # Ideally, want rectangle to start at 50,140, and be 360x360, but line thickness makes it look out of proportion
        # So these numbers make it look a little bit nicer
        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(47,137, 366,366), 6)

        # Horizontal lines
        pygame.draw.line(self.screen, (0,0,0), (50,260), (410, 260), 3)
        pygame.draw.line(self.screen, (0,0,0), (50,380), (410, 380), 3)

        # Vertical lines
        pygame.draw.line(self.screen, (0,0,0), (170,140), (170, 500), 3)
        pygame.draw.line(self.screen, (0,0,0), (290,140), (290, 500), 3)

        # Grid lines
        pygame.draw.line(self.screen, (0,0,0),(50, 180), (410, 180),1)
        pygame.draw.line(self.screen, (0,0,0),(50, 220), (410, 220),1)

        pygame.draw.line(self.screen, (0,0,0),(50, 300), (410, 300),1)
        pygame.draw.line(self.screen, (0,0,0),(50, 340), (410, 340),1)

        pygame.draw.line(self.screen, (0,0,0),(50, 420), (410, 420),1)
        pygame.draw.line(self.screen, (0,0,0),(50, 460), (410, 460),1)


        pygame.draw.line(self.screen, (0,0,0),(90, 140), (90, 500),1)
        pygame.draw.line(self.screen, (0,0,0),(130, 140), (130, 500),1)

        pygame.draw.line(self.screen, (0,0,0),(210, 140), (210, 500),1)
        pygame.draw.line(self.screen, (0,0,0),(250, 140), (250, 500),1)

        pygame.draw.line(self.screen, (0,0,0),(330, 140), (330, 500),1)
        pygame.draw.line(self.screen, (0,0,0),(370, 140), (370, 500),1)

        text = self.title.render("Sudoku", True, (0,0,0), (224,224,224))
        textRect = text.get_rect()
        textRect.center = (230, 50)
        self.screen.blit(text, textRect)

        # 162 because 160 makes it too high up, probably due to line thickness...
        # Prints currentBoard
        center = (30, 162)
        for row in range(9):
            for col in range(9):
                num = self.board[row][col]
                center = (center[0] + 40, center[1])
                if num != 0:
                    text = self.font.render(str(num), True, (0,0,0), (224,224,224))
                    textRect = text.get_rect()
                    textRect.center = center
                    self.screen.blit(text, textRect)
            center = (30, center[1] + 40)

        pygame.display.update()

if __name__ == "__main__":
    startBoard=[
        [0,0,1,5,0,0,0,0,0],
        [0,8,0,0,0,3,1,4,0],
        [0,4,0,0,8,0,0,0,3],
        [0,7,0,0,5,0,0,0,8],
        [0,0,6,9,0,8,3,0,0],
        [3,0,0,0,2,0,0,5,0],
        [5,0,0,0,7,0,0,1,0],
        [0,2,7,1,0,0,0,9,0],
        [0,0,0,0,0,4,5,0,0]
    ]

    game = Board(startBoard)
