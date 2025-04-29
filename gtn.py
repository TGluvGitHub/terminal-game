import random
import time
import game
from pathlib import Path

global r_n
r_n = ""
global g_n
g_n = ""
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

def CreateNum():
    global r_n
    global wins_count
    r_n = random.randint(1, 100)
    wins_count = 0

def save_high_score(username, wins):
    # Set the path to the leaderboards folder
    leaderboard_folder = Path("leaderboards")
    leaderboard_folder.mkdir(exist_ok=True)

    # Set file name
    file_path = leaderboard_folder / "gtn_highscore.mgtgterminalgamehighscoreleaderboard"

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

def Guess():
    start_time = time.time()
    time_limit = 120  # 2 minutes in seconds
    global wins_count

    print("You have 2 minutes to guess the number!")

    while time.time() - start_time < time_limit:
        # Show time left
        elapsed = int(time.time() - start_time)
        remaining = max(0, time_limit - elapsed)
        mins, secs = divmod(remaining, 60)
        print(f"Time left: {mins}:{secs:02d}", end='\r')

        # Ask for a guess
        try:
            g_n = int(input("\nGuess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue  # Skip the rest of the loop if input isn't a number
        
        if r_n == g_n:
            wins_count += 1  # Increment wins if correct
            print(f"Yay, you guessed the number! Total wins: {wins_count}")
            # After a win, reset the number and guess again
            CreateNum()
        elif r_n > g_n:
            print("Make it smaller")
        elif r_n < g_n:
            print("Make it bigger")

    print(f"\nTime's up! You had {wins_count} correct guesses.")
    save_high_score(game.login_user, wins_count)  # Save the score after time's up
