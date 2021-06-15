import pygame
import copy

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

def drawOutlines(screen):
    # Draws Sudoku board

    # Outer box
    # Ideally, want rectangle to start at 50,140, and be 360x360, but line thickness makes it look out of proportion
    # So these numbers make it look a little bit nicer
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(47,137, 366,366), 6)

    # Horizontal lines
    pygame.draw.line(screen, (0,0,0), (50,260), (410, 260), 3)
    pygame.draw.line(screen, (0,0,0), (50,380), (410, 380), 3)

    # Vertical lines
    pygame.draw.line(screen, (0,0,0), (170,140), (170, 500), 3)
    pygame.draw.line(screen, (0,0,0), (290,140), (290, 500), 3)

    # Grid lines
    pygame.draw.line(screen, (0,0,0),(50, 180), (410, 180),1)
    pygame.draw.line(screen, (0,0,0),(50, 220), (410, 220),1)

    pygame.draw.line(screen, (0,0,0),(50, 300), (410, 300),1)
    pygame.draw.line(screen, (0,0,0),(50, 340), (410, 340),1)

    pygame.draw.line(screen, (0,0,0),(50, 420), (410, 420),1)
    pygame.draw.line(screen, (0,0,0),(50, 460), (410, 460),1)


    pygame.draw.line(screen, (0,0,0),(90, 140), (90, 500),1)
    pygame.draw.line(screen, (0,0,0),(130, 140), (130, 500),1)

    pygame.draw.line(screen, (0,0,0),(210, 140), (210, 500),1)
    pygame.draw.line(screen, (0,0,0),(250, 140), (250, 500),1)

    pygame.draw.line(screen, (0,0,0),(330, 140), (330, 500),1)
    pygame.draw.line(screen, (0,0,0),(370, 140), (370, 500),1)


def printBoard(screen, font, guessFont, currentBoard, guessBoard):
    # Prints numbers onto the Sudoku board

    # 162 because 160 makes it too high up, probably due to line thickness...
    # Prints currentBoard
    center = (30, 162)
    for row in range(9):
        for col in range(9):
            num = currentBoard[row][col]
            center = (center[0] + 40, center[1])
            if num != 0:
                text = font.render(str(num), True, (0,0,0), (224,224,224))
                textRect = text.get_rect()
                textRect.center = center
                screen.blit(text, textRect)
        center = (30, center[1] + 40)

    # Prints guessBoard
    center = (20, 152)
    for row in range(9):
        for col in range(9):
            num = guessBoard[row][col]
            center = (center[0] + 40, center[1])
            if num != 0:
                text = smallFont.render(str(num), True, (0,0,0), (224,224,224))
                textRect = text.get_rect()
                textRect.center = center
                screen.blit(text, textRect)
        center = (20, center[1] + 40)  

def onBoard(pos):
    # Checks if cursor click is on the board
    X = pos[0]
    Y = pos[1]
    if (50 <= X <= 410) and (140 <= Y <= 500):
        return True
    return False

def gameFinished(board):
    length = len(board)
    for row in range(length):
        for col in range(length):
            if board[row][col] == 0:
                return False
    return True

if __name__ == "__main__":
    # Find answer to board
    startBoard = [
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
    # startBoard = [
    #     [4,3,5,2,6,9,7,8,1],
    #     [6,8,2,5,7,1,4,9,3],
    #     [1,9,7,8,3,4,5,6,2],
    #     [8,2,6,1,9,5,3,4,7],
    #     [3,7,4,6,8,2,9,1,5],
    #     [9,5,1,7,4,3,6,2,8],
    #     [5,1,9,3,2,6,8,7,4],
    #     [2,4,8,9,5,7,1,3,6],
    #     [7,6,3,4,1,8,2,5,0],
    # ]
    # Create a deep copy of original board
    currentBoard = [row[:] for row in startBoard]\
    # Initializes empty 2D array, used to store user guesses
    guessBoard = [[0 for col in range(9)] for row in range(9)]
    game = Board(startBoard)
    game.solve()
    answerBoard = game.board

    pygame.init()
    screen = pygame.display.set_mode((460, 600))
    icon = pygame.image.load('sudoku-svgrepo-com.svg')
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Sudoku")
    redBox = False

    # TODO: Check for valid use of these variables
    # Used to draw highlighted box, represent coordinates
    RedX = -1
    RedY = -1

    # Represent selected box, indexes for currentBoard
    SelectedX = -1
    SelectedY = -1

    # font used for currentBoard numbers, smallFont used for guesses
    font = pygame.font.SysFont('monospace',30, bold=True)
    smallFont = pygame.font.SysFont('monospace', 15)

    winFont = pygame.font.SysFont("monospace", 64, bold=True)

    run = True
    win = False
    while run:
        screen.fill((224,224,224))
        printBoard(screen, font, smallFont, currentBoard, guessBoard)
        # Rectangle begins on 50, 140
        drawOutlines(screen)

        if redBox:
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(RedX, RedY, 40, 40), 3)

        # TODO: Check if game is over
        if gameFinished(currentBoard):
            win = True
            winFont = pygame.font.SysFont("monospace", 40, bold=True)
            text = winFont.render('Congrats! You win!', True, (0,0,0), (224,224,224))
            textRect = text.get_rect()
            textRect.center = (240, 70)
            screen.blit(text, textRect)

        for event in pygame.event.get():

            # Closing Window
            if event.type == pygame.QUIT:
                run = False

            if not win:
                # Inputting a number or entering
                if event.type == pygame.KEYDOWN:
                    # This means if no box has been selected yet
                    if not redBox:
                        continue

                    # Set the value for the guess to the guessBoard
                    if event.key == pygame.K_1:
                        guessBoard[SelectedY][SelectedX] = 1
                    if event.key == pygame.K_2:
                        guessBoard[SelectedY][SelectedX] = 2                    
                    if event.key == pygame.K_3:
                        guessBoard[SelectedY][SelectedX] = 3
                    if event.key == pygame.K_4:
                        guessBoard[SelectedY][SelectedX] = 4
                    if event.key == pygame.K_5:
                        guessBoard[SelectedY][SelectedX] = 5
                    if event.key == pygame.K_6:
                        guessBoard[SelectedY][SelectedX] = 6
                    if event.key == pygame.K_7:
                        guessBoard[SelectedY][SelectedX] = 7
                    if event.key == pygame.K_8:
                        guessBoard[SelectedY][SelectedX] = 8
                    if event.key == pygame.K_9:
                        guessBoard[SelectedY][SelectedX] = 9
                    # Used to reset the guess
                    if event.key == pygame.K_0:
                        guessBoard[SelectedY][SelectedX] = 0

                    # Locking in answer
                    if event.key == pygame.K_RETURN:
                        # Check if guess exists
                        if guessBoard[SelectedY][SelectedX] == 0:
                            continue
                        elif guessBoard[SelectedY][SelectedX] == answerBoard[SelectedY][SelectedX]:
                            currentBoard[SelectedY][SelectedX] = guessBoard[SelectedY][SelectedX]
                            guessBoard[SelectedY][SelectedX] = 0
                        # User got the answer wrong
                        else:
                            guessBoard[SelectedY][SelectedX] = 0
                            print("Wrong!")

                # Clicking on Box
                if event.type == pygame.MOUSEBUTTONUP:
                    # Pos is a tuple, (X,Y)
                    pos = pygame.mouse.get_pos()
                    if onBoard(pos):

                        X = pos[0] - 50
                        Y = pos[1] - 140
                        XBox = X // 40
                        YBox = Y // 40

                        # If the spot has a number, you can't highlight it
                        if currentBoard[YBox][XBox] != 0:
                            continue

                        SelectedX = XBox
                        SelectedY = YBox
                        redBox = True
                        RedX = XBox * 40 + 50
                        RedY = YBox * 40 + 140
        pygame.display.update()

