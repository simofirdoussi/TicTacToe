Board = {'7': '.' , '8': '.' , '9': '.' ,
            '4': '.' , '5': '.' , '6': '.' ,
            '1': '.' , '2': '.' , '3': '.' }

board_keys = []

for key in Board:
    board_keys.append(key) #fill board_keys with the keys of the dictionary
    
def how_to_play():
    
    input_1 = input("Do you want to know how to play?")
    if input_1 == "y":
        print("okey here is how to play :)")
        print( "7" + ' | ' + "8"+ ' | ' + "9" )
        print('--+---+--')
        print( "4" + ' | ' + "5" + ' | ' + "6" )
        print('--+---+--')
        print( "1" + ' | ' + "2" + ' | ' + "3" )
        print("Enter the number of the position where yu want to set your symbol ")
        print("**************************")
        print("Good luck! :)") 
        print("**************************")
    else:
        print("**************************")
        print("Okey, good luck then! :)") 
        print("**************************")
      


def printBoard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])

#tha main function
def game():

    turn = 'X'
    count = 0  #initialize a counter
    how_to_play()

    while True:
        
        printBoard(Board)
        print("It's your turn," + turn + ".Move to which place?")

        move = input() # get the kayboard input      

        if  Board[move] == '.':
            Board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ': # across the top
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ': # across the middle
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ': # across the bottom
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ': # down the left side
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ': # down the middle
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ': # down the right side
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif Board['7'] == Board['5'] == Board['3'] != ' ': # diagonal
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ': # diagonal
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            Board[key] = "."

        game()

if __name__ == "__main__":
    game()
