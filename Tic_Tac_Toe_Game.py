'''
This is a program for a simple Tic-Tac-Toe game.
The board layout is as follows:

   |   |   
 7 | 8 | 9 
___|___|___
   |   |
 4 | 5 | 6
___|___|___
   |   |   
 1 | 2 | 3
   |   |
   
The actual board will be of list type having index from 0-9.
(note: here the 0 index is reserved as '#' so index 1 - 9 are available for positons on the board).
The numbers in the board above correspond to the number positions on the numpad of a keyboard.
These numbers are used as a reference to place marks by players on their turn to these positions on the board.
'''

import random


def display_board(board):
       
    '''
    Takes input : a board of list type
    Output : prints out the updated board
    This function will be used to display the game board.
    After every move by the players, the board will be re-printed.
    To clear the screen before the new/updated board is printed, 100 blank lines (\n) are printed.
    '''
    
    print('\n' * 100) # Printing blank lines to clear screen
    
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('___|___|___')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('___|___|___')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')


def player_input():
    
    '''
    Takes no input argument
    Output : returns a tuple of character markers.
    Function to ask players if they want the (X) or (O) marker.
    The input marker is assigned to player1.
    '''
    
    choice = str()
    while choice != 'X' and choice != 'O': # while loop for getting valid inputs from players
        choice = input('Enter marker for Player1: ').upper() # use of .upper() to avoid the markers in lower case

    # assigning markers to each player
    player1 = choice
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2 # default return type in this syntax is tuple, iterable which will be used later to access player markers


def place_marker(board, marker, position):
    
    '''
    Takes input : a board of list type, a character marker of a player, position to place the marker of integer type for index in list
    Output : a board of list type
    Function to place the marks by players on the board.
    '''
    
    board[position] = marker
    return board


def win_check(board, mark):
    
    '''
    Takes input : a board of list type, a character marker of a player
    Output : boolean value, true if a player wins, false if no one wins
    Function to check for winning conditions and deciding which player wins
    '''
    
    # check for horizontal win conditions
    if board[7] == board[8] == board[9] == mark:
        print(f'{mark} wins')
        return True
    elif board[4] == board[5] == board[6] == mark:
        print(f'{mark} wins')
        return True
    elif board[1] == board[2] == board[3] == mark:
        print(f'{mark} wins')
        return True
    
    # check for vertical win conditions
    elif board[7] == board[4] == board[1] == mark:
        print(f'{mark} wins')
        return True
    elif board[8] == board[5] == board[2] == mark:
        print(f'{mark} wins')
        return True
    elif board[9] == board[6] == board[3] == mark:
        print(f'{mark} wins')
        return True
    
    # check for diagonals
    elif board[7] == board[5] == board[3] == mark:
        print(f'{mark} wins')
        return True
    elif board[1] == board[5] == board[9] == mark:
        print(f'{mark} wins')
        return True
    
    # no condition satisfies / draw
    else:
        return False


def choose_first():
    
    '''
    Takes no input argument
    Output : a random value either 1 or 2
    Function to decide which player gets to play first
    '''
    
    return random.randint(1, 2)


def space_check(board, position):
    
    '''
    Takes input : a board of list type, integer value for index position
    Output : boolean value, true if position on the board is empty, false otherwise
    Function to check if the position is empty/available to place a marker for the player's turn
    '''
    
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True


def full_board_check(board):
    
    '''
    Takes input : a board of list type
    Output : boolean value, true if board is full, false otherwise
    Function to check if the board is completely full and no place is available to place a marker
    '''
    
    for mark in board:
        if mark == ' ':
            return False
    else:
        return True


def player_choice(board):
    
    '''
    Takes input : a board of list type
    Output : returns position to place the marker on the board
    Function to take in a value for position to place marker on the board and return that position index if space is available
    '''
    
    choice = eval(input('Enter position to put your mark : '))
    if space_check(board, choice):
        return choice
    else:
        pass


def replay():
    
    '''
    Takes no input
    Output calls function to replay the game, returns false if no
    Function to ask the players for a rematch/new game
    '''
    
    rep = input('Do you want to play again? \nYes / No: ')
    if rep.lower() == 'yes' or rep.lower() == 'y':
        play_game()
    else:
        return False


def play_game():
    print('Welcome to Tic-Tac-Toe game: ')
    board = [' '] * 10
    board[0] = '#'
    display_board(board)
    # Deciding symbols for players
    mark = player_input()
    Player1 = mark[0]
    Player2 = mark[1]

    # Deciding turns
    first_turn = choose_first()
    turn = first_turn
    # Start the game
    while True:
        if turn == 1:
            print('Player 1\'s turn')
            if not full_board_check(board):
                place_marker(board, Player1, player_choice(board))
                display_board(board)
                turn = 2
        else:
            print('Player 2\'s turn')
            if not full_board_check(board):
                place_marker(board, Player2, player_choice(board))
                display_board(board)
                turn = 1

        if full_board_check(board) and not win_check(board, Player1) and not win_check(board, Player2):
            print('It\'s a Draw')
            break
        if win_check(board, Player1) or win_check(board, Player2):
            break
    if not replay():
        print('Thank you for playing')


# Now to play the game
if __name__ == "__main__":
    play_game()
