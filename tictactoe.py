# function to build the board 
board=['-' for i in range(9)]
def display_board():
    print('|',board[0],'|',board[1],'|',board[2],'|')
    print('|',board[3],'|',board[4],'|',board[5],'|')
    print('|',board[6],'|',board[7],'|',board[8],'|')

# settign plater 1 as 'x' and player2 as 'o'
player1='x'
player2='o'

# winning condition for the players 
def win_condition(player):
    condition=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for check in condition:
        if board[check[0]]== player and board[check[1]]==player and board[check[2]]==player:
            return True
    else:
        return  False
win = True
def tictac():
    while win:
    
        while True:
            # getting a input number from the player1
            player_1=int(input(f'{player1} enter the choice:'))

            if player_1 not in  range(1,10):
                print("pls enter the value between 1 and 9:")
                continue
            if board[player_1 - 1] =="-":
                board[player_1 - 1] = player1
                display_board()
                if win_condition(player1):
                    return f'{player1} is the winner '
            
                break
            else:
                print('the space is already filled')
        while True:
            # gettign a input number from the player2
            player_2=int(input(f"{player2}   enter the value:"))
            if player_2 not in range(1,10):
                print("pls enter the value between 1 and 9:")
                continue
            if board[player_2 - 1]=='-':
                board[player_2 - 1]= player2
                display_board()
                if win_condition(player2):
                    return f'{player2} is the winner'
                break
            else:
                print("the space is not empty")
print(tictac())
            