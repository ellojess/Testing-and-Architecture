
# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

def drawBoard(board):
    """This function prints out the board that it was passed.
    board" is a list of 10 strings representing the board (ignore index 0)"""
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    """Lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item, and the computer's letter as the second."""
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def whoGoesFirst():
    """Randomly choose the player who goes first."""
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    """Given a board and a player’s letter, this function returns True if that player has won.
    We use bo instead of board and le instead of letter so we don’t have to type as much."""
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle    # TODO: Fix the indentation of this lines and the following ones ✅
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    """Make a duplicate of the board list and return it the duplicate."""
    dupeBoard = []

    for i in range(len(board)): # TODO: Clean this mess! ✅
        dupeBoard.append(board[i])

    return dupeBoard

def isSpaceFree(board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def getPlayerMove(board):
    """Let the player type in their move."""
    playerMove = ' ' # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306 ✅
    while playerMove not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(playerMove)):
        print('What is your next move? (1-9)')
        playerMove = input()
    return int(playerMove)

def chooseRandomMoveFromList(board, movesList):
    """Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move."""
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if possibleMoves != 0: # TODO: How would you write this pythanically? (You can google for it!) ✅
        return random.choice(possibleMoves)
    # else: # TODO: is this 'else' necessary? ✅
        # return None

def getComputerMove(board, computerMove): # TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306 ✅
    """Given a board and the computer's letter, determine where to move and return that move."""
    if computerMove == 'X':
        playerMove = 'O'
    else:
        playerMove = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerMove, i)
            if isWinner(copy, computerMove):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerMove, i)
            if isWinner(copy, playerMove):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None: # TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.) ✅
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    """Return True if every space on the board has been taken. Otherwise return False."""
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

# TODO: The following mega code block is a huge hairy monster. Break it down 
# into smaller methods. ✅ Use TODO s and the comment above each section as a guide 
# for refactoring. ✅

def isGamePlaying():
    """Check if game is being played and determine actions and turns between computer and person"""
    # gameIsPlaying = True # TODO: Study how this variable is used. Does it ring a bell? (which refactoring method?) 
                         #       See whether you can get rid of this 'flag' variable. If so, remove it. ✅
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    
    while True: # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
                         #       Use a meaningful name for the function you choose. ✅
        if turn == 'player':
            # Player’s turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                # gameIsPlaying = False
                break
            # else:  # TODO: is this 'else' necessary? ✅
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print('The game is a tie!')
                break
                # else:  # TODO: Is this 'else' necessary? ✅
            turn = 'computer'

        else:
            # Computer’s turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                # gameIsPlaying = False
                break 
            # else:     # TODO: is this 'else' necessary? ✅
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print('The game is a tie!')
                break
                # else: # TODO: Is this 'else' necessary? ✅
            turn = 'player'

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10 # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.) ✅
                          # Note - Worth leaving as is since 10 only has a single occurrence
    playerLetter, computerLetter = inputPlayerLetter()

    isGamePlaying()

    if not playAgain():
        break