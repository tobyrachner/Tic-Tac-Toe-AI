from minimax import minimax

DEFAULT_BOARD = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def getInput(board):
    while True:
        cell = input("Select a cell (0-8) or 'q' to quit: ")
        if cell == 'q':
            return 'quit'
        if cell.isnumeric() and int(cell) in range(9) and type(board[int(cell)]) == int:
            return int(cell)
        else:
            print('Invalid input')

def getStartingPosition():
    while True:
        i = input('Do you want to go first or second? (1/2): ')
        if i == '1': return 'X', 'O'
        if i == '2': return 'O', 'X'
        print('invalid input')

def PrettyPrint(board):
    board = board.copy()
    for i in range(len(board)):
        if type(board[i]) == int:
            board[i] = ' '
        
    print("---+---+---")
    print("", board[0], "|", board[1], "|", board[2])
    print("---+---+---")
    print("", board[3], "|", board[4], "|", board[5])
    print("---+---+---")
    print("", board[6], "|", board[7], "|", board[8])
    print("---+---+---")
    return board

def changePlayer(player):
    if player == 'O': return 'X'
    if player == 'X': return 'O'

def getWinner(board, player):
    if (board[0] == board[1] == board[2] == player or
    board[3] == board[4] == board[5] == player or
    board[6] == board[7] == board[8] == player or
    board[0] == board[3] == board[6] == player or
    board[1] == board[4] == board[7] == player or
    board[2] == board[5] == board[8] == player or
    board[0] == board[4] == board[8] == player or
    board[2] == board[4] == board[6] == player):
        return True
    else:
        return False
   
def checkDraw(board):
    emptyCells = [x for x in board  if type(x) == int]
    if len(emptyCells) == 0: return True

def main():
    currBoard = DEFAULT_BOARD
    currPlayer = 'X'
    humanMark, aiMark = getStartingPosition()

    while True:
        PrettyPrint(currBoard)

        if currPlayer == humanMark:
            cell = getInput(currBoard)
            if cell == 'quit':
                print('Game cancelled')
                break
        else:
            cell = minimax(currBoard, aiMark, -300, 300)[0]
            print('The AI chose cell', cell)

        currBoard[cell] = currPlayer
       
        if getWinner(currBoard, currPlayer):
            PrettyPrint(currBoard)
            if currPlayer == humanMark:
                print('You win!')
            else:
                print("You lose.")
            break

        if checkDraw(currBoard):
            print("It's a tie!")
            break

        currPlayer = changePlayer(currPlayer)

if __name__ == '__main__':
    main()
