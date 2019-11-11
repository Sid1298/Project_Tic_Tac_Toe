import random


def display_board(board):
    print('\n' * 100)
    '''print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])'''
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
    choice = ''
    while choice != 'X' and choice != 'O':
        choice = input('Enter marker for Player1: ').upper()

    player1 = choice
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    # m = mark == 'X'
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
    # no condition satisfies
    else:
        return False


def choose_first():
    return random.randint(1, 2)


def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True


def full_board_check(board):
    for mark in board:
        if mark == ' ':
            return False
    else:
        return True


def player_choice(board):
    choice = eval(input('Enter position to put your mark : '))
    if space_check(board, choice):
        return choice
    else:
        pass


def replay():
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


play_game()
