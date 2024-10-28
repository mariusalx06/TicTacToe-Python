board = ["-", "-", "-",
         "-","-","-",
         "-","-","-"]
gameIsOn = True
current_player = ""

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "      " + "1|2|3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "      " + "4|5|6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "      " + "7|8|9")

display_board()

def start_game():
    global current_player
    choice = input("Select Player - X or O:\n")
    if choice == "X" or choice == "x":
        p1 = "X"
        play_game(p1)
    elif choice == "O" or choice == "o":
        p1 = "O"
        play_game(p1)
    else:
        return start_game()

def switch_player():
    global current_player
    if current_player =="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return current_player

def play_game(p1):
    global gameIsOn
    global current_player
    global board
    current_player = p1

    while gameIsOn:
        print("Current player " +current_player)
        position = input("Choose position from 1 - 9: ")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose position from 1 - 9: ")
        position = int(position) - 1
        if board[position] == "-":
            board[position] = current_player
            display_board()
            if board[0] == board[1] == board[2] != "-":
                gameIsOn = False
                print("Congratulations " + board[0] + " you WON!")
            elif board[3] == board[4] == board[5] != "-":
                gameIsOn = False
                print("Congratulations " + board[3] + " you WON!")
            elif board[6] == board[7] == board[8] != "-":
                gameIsOn = False
                print("Congratulations " + board[6] + " you WON!")
            elif board[0] == board[3] == board[6] != "-":
                gameIsOn = False
                print("Congratulations " + board[0] + " you WON!")
            elif board[1] == board[4] == board[7] != "-":
                gameIsOn = False
                print("Congratulations " + board[1] + " you WON!")
            elif board[2] == board[5] == board[8] != "-":
                gameIsOn = False
                print("Congratulations " + board[2] + " you WON!")
            elif board[0] == board[4] == board[8] != "-":
                gameIsOn = False
                print("Congratulations " + board[0] + " you WON!")
            elif board[2] == board[4] == board[6] != "-":
                gameIsOn = False
                print("Congratulations " + board[6] + " you WON!")
            elif "-" not in board:
                gameIsOn = False
                print("It's a Tie")
            current_player = switch_player()
        else:
            print("Position already selected, choose another position!")
    if not gameIsOn:
        restart = input("Want to go again? Press Y or N\n")
        while restart not in ["y","Y","N","n"]:
            restart = input("Want to go again? Press Y or N\n")
        if restart == "Y" or restart == "y":
            gameIsOn = True
            board = ["-", "-", "-",
                     "-", "-", "-",
                     "-", "-", "-"]
            start_game()
        elif restart == "N" or restart == "n":
            print("See you next time!")

start_game()