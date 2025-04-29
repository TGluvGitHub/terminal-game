import random
import time
from pathlib import Path

global wins_count

def countdown_timer(seconds):
    start_time = time.time()
    while seconds > 0:
        elapsed = int(time.time() - start_time)
        remaining = max(0, seconds - elapsed)
        mins, secs = divmod(remaining, 60)
        print(f"Time left: {mins}:{secs:02d}", end='\r')
        time.sleep(1)  # Update every second
        if remaining == 0:
            break
    print("\nTime's up!")  # Ensure it prints when time is up

def save_high_score(username, wins):
    leaderboard_folder = Path("leaderboards")
    leaderboard_folder.mkdir(exist_ok=True)

    # Set file name
    file_path = leaderboard_folder / "ttt_highscore.mgtgterminalgamehighscoreleaderboard"

    # Read old scores
    scores = {}
    if file_path.exists():
        with open(file_path, "r") as file:
            for line in file:
                name, s = line.strip().split(",")
                scores[name] = int(s)

    # Update user's score if it's better
    if username not in scores or wins > scores[username]:
        scores[username] = wins

    # Save all scores back
    with open(file_path, "w") as file:
        for name, s in scores.items():
            file.write(f"{name},{s}\n")

    print("High score saved!")

    # Print the leaderboard sorted by score (highest to lowest)
    print("\n--- Leaderboard ---")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(sorted_scores, start=1):
        print(f"{i}. {name}: {score} wins")

def PlayTicTacToeTimed(username):
    global wins_count
    wins_count = 0
    time_limit = 120  # 2 minutes

    # Simulate the game loop for Tic Tac Toe
    print("Welcome to Tic Tac Toe! You have 2 minutes to play.")

    start_time = time.time()

    while time.time() - start_time < time_limit:
        # Display time left
        elapsed = int(time.time() - start_time)
        remaining = max(0, time_limit - elapsed)
        mins, secs = divmod(remaining, 60)
        print(f"Time left: {mins}:{secs:02d}", end='\r')

        # Simulate a turn (replace with actual game logic)
        user_input = input("Enter your move (X or O): ")
        if user_input == "X":  # Simulate a win
            wins_count += 1
            print(f"Correct! Wins: {wins_count}")
        elif user_input == "O":  # Simulate a loss
            print("Try again!")
        else:
            print("Invalid move. Enter X or O.")

    print(f"\nTime's up! You had {wins_count} wins.")
    save_high_score(username, wins_count)  # Save the score after time's up
