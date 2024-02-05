import random

testBoards = [
    ["X", 1, "O", "X", 4, "X", "O", "O", 8],
    ["X", 1, 2, 3, 'O', 5, 'O', 7, 'X'],
    ["X", "O", "X", 3, 'O', 5, 'O', 7, 'X'],
    ["O", 1, 2, 3, 'X', 5, 6, 7, 'O'],
    ["O", 1, 2, 3, 4, 5, 6, 7, 8]]
inputBoard = testBoards[4]
humanMark = 'O'
aiMark = 'X'

def emptyCells(board):
    return [x for x in board if type(x) == int]

def changePlayer(currPlayer):
    if currPlayer == 'X':
        return 'O'
    if currPlayer == 'O':
        return 'X'

def determineWinner(board, player):
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
   
def minimax(currBoard, currPlayer, alpha, beta, depth = -1, run = 0, aiMark = '', humanMark = ''):
    if currBoard == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return random.choice(currBoard), 1
    if depth == -1:
        aiMark = currPlayer
        humanMark = changePlayer(aiMark)
    depth += 1
    run += 1

    availCells = emptyCells(currBoard)
    random.shuffle(availCells)

    if determineWinner(currBoard, humanMark):
        return -10, run
    if determineWinner(currBoard, aiMark):
        return 10, run
    if len(availCells) == 0:
        return 0, run
   
    testRecords = []
    lowestScore = 100
    highestScore = -100
   
    for Cell in availCells:
        testBoard = currBoard.copy()
        testBoard[Cell] = currPlayer
        result, run = minimax(testBoard, changePlayer(currPlayer), alpha, beta, depth=depth, run=run, aiMark=aiMark, humanMark=humanMark)
        testRecords.append((Cell, result))
        if currPlayer == aiMark:
            highestScore = max(highestScore, result)
            alpha = max(highestScore, alpha)
            if beta <= alpha:
                break
        if currPlayer == humanMark:
            lowestScore = min(lowestScore, result)
            beta = min(lowestScore, beta)
            if beta <= alpha:
                break

    if depth == 0:
        bestMove = (0, -100)
        for move in testRecords:
            if move[1] > bestMove[1]:
                bestMove = move
        return bestMove[0], run
   
    if currPlayer == aiMark:
        return highestScore, run
   
    if currPlayer == humanMark:
        return lowestScore, run
