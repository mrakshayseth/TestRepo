from random import randrange
global board
i=0
j=0
board = [[i for i in range(3)]for j in range (3)]
global cell_values
cell_value = {}
counter = 0
for i in range(3):
    for j in range(3):
        counter += 1
        board[i][j]=counter
        cell_value[counter]=(i,j)
occupied_field = {}
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    a=0
    b=1
    c=2
    for i in range(3):
        print ("+-----+-----+-----+")
        print ("|     |     |     |")    
        print ("| ",board[i][a]," | ",board[i][b]," | ",board[i][c]," | ")
        print ("|     |     |     |")
    print ("+-----+-----+-----+")
    
def move_mod(move,sign):
    if move in cell_value.keys()and move not in occupied_field.keys():
        i=cell_value[move][0]
        j=cell_value[move][1]
        board[i][j]=sign
        occupied_field[move] = cell_value[move]
        return True
    elif len(cell_value)==len(occupied_field):
        return True
    else:
        return False
    
def player_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    try:
        move= int(input("Enter your move: "))
        sign="o"
        x= move_mod(move,sign)
        if x==False:
            print("illigal move")
            player_move(board)
    except:
        print("illigal move")
        player_move(board)
    #display_board(board)

#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    #free_field = []
    

def victory_for(board):
    
    for i in range (3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            print ("victory for:",board[i][1])
            display_board(board)
            return True
            break
        elif board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            print ("victory for:",board[1][i])
            display_board(board)
            return True
            break
    if board[0][0]==board[1][1]and board[1][1]==board[2][2] or board[2][0]==board[1][1]and board[1][1]==board[0][2]:
        print ("victory for:",board[1][1])
        display_board(board)
        return True
    if len(occupied_field)==len(cell_value) and len(occoupied_field)==9:
        print ("Game Tie")
        display_board(board)
        return True
    else:
        return False
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    from random import randrange
    move=999
    move = randrange(8)+1
    sign="x"
    x=move_mod(move,sign)
    if x==False:
        draw_move(board)

    # The function draws the computer's move and updates the board.

while victory_for(board)==False:
    display_board(board)
    player_move(board)
    draw_move(board)
    


