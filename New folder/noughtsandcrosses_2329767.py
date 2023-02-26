
import random
import os.path
import json
random.seed()

def draw_board(board):

    row_border = " ----------- "
    print(row_border) 
    for row in board: 
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print(row_border)

def welcome(board):

    print('Welcome to the "Unbeatable Noughts and Crosses game.')
    print('The board layout is shown below:')
    draw_board(board)
    print('When prompted, enter the number corresponding to the square you want')

def initialise_board(board):
   
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
    return board

def get_player_move(board):
   
    while True:
        try:
            player_move = int(input("Enter your move [1-9]: ")) - 1
            if 0 <= player_move <= 8:
                col = 0 if player_move % 3 == 0 else (1 if player_move % 3 == 1 else 2)
                row = 0 if 0 <= player_move <=2 else (1 if 3 <= player_move <=5 else 2)
                if board[row][col] != " ":
                    print("cell already used")
                    continue
                break
            raise ValueError("Number must be between 1 to 9")
        except ValueError:
            print("enter a valid number between 1 to 9")
    return row, col

def choose_computer_move(board):
   
    clone_board = board.copy()
    row, col = 0,0

    #check if computer can win in the next move
    for i in range(3):
        for j in range(3):
            if clone_board[i][j] == " ":
                clone_board[i][j] = "O"
                if check_for_win(board, "O"):
                    row, col = i, j
                    return row, col
                clone_board[i][j] = " "

    #check if player can win in the next move, then block
    for i in range(3):
        for j in range(3):
            if clone_board[i][j] == " ":
                clone_board[i][j] = "X"
                if check_for_win(board, "X"):
                    row, col = i, j
                    return row, col
                clone_board[i][j] = " "

    if clone_board[1][1] == " ":
        row, col = 1, 1
        return row, col

    # check empty 4 corners
    for i in [0,2]:
        for j in [0,2]:
            if clone_board[i][j] == " ":
                row, col = i, j
                return row, col

    for i in range(3):
        for j in range(3):
            if clone_board[i][j] == " ":
                row, col = i, j
                return row, col


def check_for_win(board, mark):
   
    win_conditions = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
    ]
    for win in win_conditions:
        cell0_r, cell0_c = win[0]
        cell1_r, cell1_c = win[1]
        cell2_r, cell2_c = win[2]
        if (
            board[cell0_r][cell0_c] == mark and
            board[cell1_r][cell1_c] == mark and
            board[cell2_r][cell2_c] == mark
        ):
            return True
    return False

def check_for_draw(board):

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def play_game(board):
 
    board = initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            return 1
        if check_for_draw(board):
            return 0
        row, col = choose_computer_move(board)
        board[row][col] = "O"
        draw_board(board)
        if check_for_win(board, "O"):
            return -1
        if check_for_draw(board):
            return 0

def menu():
  
    choice = ""
    while True:
        try:
            display_message = """Enter one of the following options: 
                        1 - play the game
                        2 - Save your score in the leaderboard
                        3 - Load and display the leaderboard
                        q - End the program"""
            print(display_message)
            choice = input("1, 2, 3, or q? ")
            if choice in ["1", "2", "3", "q", "Q"]:
                break
            raise ValueError("invalid input")
        except ValueError:
            print("user choice invalid")
    return choice

def load_scores():
  
    file_path = os.path.join(os.path.dirname(__file__), "/leaderboard.txt")
    try:
        with open("leaderboard.txt", "r", encoding="utf8") as file:
            file_content = file.read()
            leaders = json.loads(file_content)
    except IOError:
        print("Error reading leaderboard.txt")
    return leaders

def save_score(score):
   
    leaders = load_scores()
    while True:
        try:
            user_name = input("Enter your name: ")
            if user_name == "":
                raise EOFError
            file_path = os.path.join(os.path.dirname(__file__), "/leaderboard.txt")
            with open("leaderboard.txt", "w", encoding="utf8") as file:
                leaders[user_name] = score
                file_content = json.dumps(leaders)
                file.write(file_content)
                break
        except EOFError:
            print("invalid input")


def display_leaderboard(leaders):
  
    print("Leaderboard")
    for key, value in leaders.items():
        print(f"{key}: {value}")
print((os.path.abspath(__file__)+"\\leaderboard.txt"))