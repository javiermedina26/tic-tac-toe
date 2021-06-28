import os

''' This example was taken on https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874,
    this game is for 2 pleople.
    Here you can see Handling List, Dictionary, Functions, Package and Loops'''

def ClearScreen():
    os.system('cls')

TicTac = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def InitializeGrid():
    return {
        '7': ' ', '8': ' ', '9': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '1': ' ', '2': ' ', '3': ' '
    }

count = 0

def ShowTicTacToe(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def ValidationVictory(counter, board, turn):
    flag = False

    if counter >= 5:
        if board['1'] == board['4'] == board['7'] != ' ': #vertical 1
            ShowTicTacToe(board)
            print("Game Over!")
            print(" **** " + turn + " won. ****")
            flag = True
        elif board['2'] == board['5'] == board['8'] != ' ': #vertical 2
            ShowTicTacToe(board)
            print("Game Over!")
            print(" **** " + turn + " won. ****")
            flag = True
        elif board['3'] == board['6'] == board['9'] != ' ': #vertical 3
            ShowTicTacToe(board)
            print("Game Over!")
            print(" **** " + turn + " won. ****")
            flag = True
        elif board['1'] == board['2'] == board['3'] != ' ': #horizontal 1
            ShowTicTacToe(board)
            print("Game Over!")
            print(" **** " + turn + " won. ****")
            flag = True
        elif board['4'] == board['5'] == board['6'] != ' ': #horizontal 2
            ShowTicTacToe(board)
            print("Game Over!")
            print(" **** " + turn + " won. ****")
            flag = True
        elif board['7'] == board['8'] == board['9'] != ' ': #horizontal 3
            ShowTicTacToe(board)
            print("Game Over!")
            print(" **** " + turn + " won. ****")
            flag = True
        elif board['1'] == board['5'] == board['9'] != ' ': #diagonal 1
            ShowTicTacToe(board)
            print("Game Over!")
            print(" **** " + turn + " won. ****")
            flag = True
        elif board['3'] == board['5'] == board['7'] != ' ': #diagonal 2
            ShowTicTacToe(board)
            print("Game Over!")
            print(" **** " + turn + " won. ****")
            flag = True
    if counter == 9:
        ClearScreen()
        ShowTicTacToe(board)
        print("\nGame Over.\n")
        print("It's a tie!!!")
        flag = True

    return flag

def StartGame():
    turn = 'X'
    counter = 0
    grid = InitializeGrid()

    ClearScreen()

    for i in range(10):
        ClearScreen()
        ShowTicTacToe(grid)

        print('Input your move: ')
        move = input()

        if move in TicTac:
            if grid[move] == ' ':
                grid[move] = turn
                counter += 1
            else:
                print('You have to move in another position. Press any to continue...')
                input()
                continue
        else:
            print('You have to input numeric value 0-9. Press any to continue...')
            input()
            continue

        flag = ValidationVictory(counter, grid, turn)

        if flag:
            break  

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

# Start game

while True:
    print("Do you want to play (Y/N)?")
    option = input()

    if option.upper() in ['Y', 'N']:
        if option.upper() == 'Y':
            StartGame()
            continue
        else:
            break
    else:
        continue

