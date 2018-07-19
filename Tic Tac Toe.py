def display_board(board_data):   # step 1 display a board to play with giiven data on it
    print('   |   |')
    print(' ' + board_data[7] + ' | ' + board_data[8] + ' | ' + board_data[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board_data[4] + ' | ' + board_data[5] + ' | ' + board_data[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board_data[1] + ' | ' + board_data[2] + ' | ' + board_data[3])
    print('   |   |')

#step2 take input in 'X' or '0'and return seletion, keep asking for the input until player answers
def player_input():
    selection= ' '
    while not ( selection == 'X' or selection == '0'):
        selection = input('player 1: Do you want to be X or 0?').upper()
    # decide marker for eack plaeyer if one wants  x than other will automatically get 0 or vice versa
    if selection == 'X':
        return ('X' , '0')
    else:
        return ('0' , 'X')

#step 3: a function takes board list ,marker or above selection and position
def place_marker(board,marker,postion):
    board[postion]=marker

#step 4:function that will decide winner
#player mark would be 0 or X to check which one is a winner by comparing some constraints
def win_check(board,player_mark):
    return ((board[7] == player_mark and board[8] == player_mark and board[9] == player_mark)
    or (board[4] == player_mark and board[5] == player_mark and board[6] == player_mark)
    or (board[1] == player_mark and board[2] == player_mark and board[3] == player_mark)
    or (board[7] == player_mark and board[4] == player_mark and board[1] == player_mark)
    or (board[8] == player_mark and board[5] == player_mark and board[2] == player_mark)
    or (board[9] == player_mark and board[6] == player_mark and board[3] == player_mark)
    or (board[7] == player_mark and board[5] == player_mark and board[3] == player_mark)
    or (board[9] == player_mark and board[5] == player_mark and board[1] == player_mark))
#step 5:create a function to decide which player goes first
import random
def choose_turn():
    if random.randint(0,1) == 0:
        return 'player 2'
    else:
        return 'player 1'

#step 6 :function to decide whether space s available or not it'll return true if required position is empty
def space_check(board,position):
    return board[position] == ' '

# step 7 : function will check the board is full or empty
def full_board_check(board):
    for items in range(0,10):
       if space_check(board,items):
           return False
    return True

#step 8 :function asks from  a player the next position to be filled and checks is it available
def ask_position_n_check(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose your next position...(1-9)'))
    return position

#step 9: function will ask the player if they want to play again return true if yes
def replay():
    return input('Do you want to play again...(Yes or No').lower().startswith('y')

#step 10 : hard part : here we use while loop to run a game by writing a last code

print('Welcome to Tic Tac Toe!!!')
while True:
    #Reset the Board
    theboard = 10 * [ ' ']
    player1_marker,player2_marker =player_input() #to decide wich player wants 0 marker or which want X marker
    turn=choose_turn()
    print(turn + 'will go first...')
    play_game = input('Are you ready to play...?Enter yes or no')
    if play_game.lower()[0]== 'y':
        game_on =True
    else:
        game_on =False

    while game_on:
        if turn == 'player 1':
            #player 1 turn
            display_board(theboard)
            position = ask_position_n_check(theboard)
            place_marker(theboard,player1_marker,position)

            if win_check(theboard,player1_marker):
                display_board(theboard)
                print(" congratulations!! you have on the game")
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('the game is a draw!')
                    break
                else:
                    turn = 'player 2'

        else:
            # player 2 turn
            display_board( theboard )
            position = ask_position_n_check(theboard)
            place_marker(theboard, player2_marker, position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print(" congratulations!! you have won the game")
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('the game is a draw!')
                    break
                else:
                    turn = 'player 1'
    if not replay():
        break





'''output would be
Welcome to Tic Tac Toe!!!
player 1: Do you want to be X or 0?x
player 1will go first...
Are you ready to play...?Enter yes or noy
   |   |
   |   |  
   |   |
-----------
   |   |
   |   |  
   |   |
-----------
   |   |
   |   |  
   |   |
choose your next position...(1-9)5
   |   |
   |   |  
   |   |
-----------
   |   |
   | X |  
   |   |
-----------
   |   |
   |   |  
   |   |
choose your next position...(1-9)6
   |   |
   |   |  
   |   |
-----------
   |   |
   | X | 0
   |   |
-----------
   |   |
   |   |  
   |   |
choose your next position...(1-9)7
   |   |
 X |   |  
   |   |
-----------
   |   |
   | X | 0
   |   |
-----------
   |   |
   |   |  
   |   |
choose your next position...(1-9)3
   |   |
 X |   |  
   |   |
-----------
   |   |
   | X | 0
   |   |
-----------
   |   |
   |   | 0
   |   |
choose your next position...(1-9)1
   |   |
 X |   |  
   |   |
-----------
   |   |
   | X | 0
   |   |
-----------
   |   |
 X |   | 0
   |   |
choose your next position...(1-9)7
choose your next position...(1-9)6
choose your next position...(1-9)3
choose your next position...(1-9)2
   |   |
 X |   |  
   |   |
-----------
   |   |
   | X | 0
   |   |
-----------
   |   |
 X | 0 | 0
   |   |
choose your next position...(1-9)4
   |   |
 X |   |  
   |   |
-----------
   |   |
 X | X | 0
   |   |
-----------
   |   |
 X | 0 | 0
   |   |
 congratulations!! you have on the game
Do you want to play again...(Yes or Noy
player 1: Do you want to be X or 0?'''