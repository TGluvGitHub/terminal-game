import __main__
from pathlib import Path
import time
import random

login_user = ""
current_player = ""
current_player = login_user
board = ['','','','','','','','','','','']

def printBoard():
    print()
    print(board[0] or "0", "|", board[1] or "1", "|", board[2] or "2")
    print("--+---+--")
    print(board[3] or "3", "|", board[4] or "4", "|", board[5] or "5")
    print("--+---+--")
    print(board[6] or "6", "|", board[7] or "7", "|", board[8] or "8")
    print()

def checkIsOver():
    if (board[0] == board[1] == board[2]) and board[0] != "":
        return board[0]
    if (board[3] == board[4] == board[5]) and board[3] != "":
        return board[3]
    if (board[6] == board[7] == board[8]) and board[6] != "":
        return board[6]
    if (board[0] == board[3] == board[6]) and board[0] != "":
        return board[0]
    if (board[1] == board[4] == board[7]) and board[1] != "":
        return board[1]
    if (board[2] == board[5] == board[8]) and board[2] != "":
        return board[2]
    if (board[0] == board[4] == board[8]) and board[0] != "":
        return board[0]
    if (board[2] == board[4] == board[6]) and board[2] != "":
        return board[2]
    return None

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def find_winning_move(player_mark):
    for i in range(9):
        if board[i] == "":
            board[i] = player_mark
            if checkIsOver() == player_mark:
                board[i] = ""
                return i
            board[i] = ""
    return None

def GameLoopTTT(login_user):
    current_player = login_user
    game_over = False

    while not game_over:
        printBoard()

        if current_player == login_user:
            try:
                input_move = int(input(current_player + ", what is your move? "))
                if input_move < 0 or input_move > 8 or board[input_move] != "":
                    print("Invalid move! Try again.")
                    continue
                board[input_move] = 'X'
            except (ValueError, IndexError):
                print("Invalid input! Choose a number between 0 and 8.")
                continue
        else:
            move = find_winning_move('O')  # Try to win
            if move is None:
                move = find_winning_move('X')  # Try to block player
            if move is None:
                empty_spaces = [i for i in range(9) if board[i] == ""]
                if empty_spaces:
                    move = random.choice(empty_spaces)
            if move is not None:
                board[move] = 'O'
                print("AI moved at position", move)

        winner = checkIsOver()
        if winner == "X":
            printBoard()
            print("Player X (" + login_user + ") Wins!")
            return login_user
        elif winner == "O":
            printBoard()
            print("Player O (AI) Wins!")
            return "AI"

        if all(cell != "" for cell in board):
            printBoard()
            print("It's a draw!")
            return None

        current_player = "AI" if current_player == login_user else login_user

    return None

def PlayTicTacToeTimed(login_user):
    start_time = time.time()
    time_limit = 120  # 2 minutes
    wins = 0

    while time.time() - start_time < time_limit:
        winner = GameLoopTTT(login_user)
        if winner == login_user:
            wins += 1

        for i in range(9):
            board[i] = ""

        elapsed = time.time() - start_time
        remaining = int(time_limit - elapsed)
        mins, secs = divmod(remaining, 60)
        print(f"Time left: {mins}:{secs:02d}")
        print("Current wins:", wins)

    print("\nTime's up!")
    print("Total Wins:", wins)
    save_high_score(login_user, wins)

def save_high_score(username, score):
    leaderboard_folder = Path("leaderboards")
    leaderboard_folder.mkdir(exist_ok=True)

    file_path = leaderboard_folder / "ttt_highscore.mgtgterminalgamehighscoreleaderboard"

    scores = {}
    if file_path.exists():
        with open(file_path, "r") as file:
            for line in file:
                name, s = line.strip().split(",")
                scores[name] = int(s)

    if username not in scores or score > scores[username]:
        scores[username] = score

    with open(file_path, "w") as file:
        for name, s in scores.items():
            file.write(f"{name},{s}\n")

    print("High score saved!")

    print("\n--- Leaderboard ---")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(sorted_scores, start=1):
        print(f"{i}. {name}: {score}")

