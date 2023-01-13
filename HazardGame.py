from tqdm import tqdm
import random
import time

def game():
    print("Welcome to the Hazard Game!")
    time.sleep(1)
    print("Collect as many coins as you can while avoiding obstacles...")
    time.sleep(1)
    print("Ready? Go!")
    time.sleep(1)

    score = 0
    coins = 0
    obstacles = ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|"]
    for obstacle in tqdm(obstacles, desc="Score: {} | Coins: {}".format(score, coins)):
        print("_"*score, obstacle)
        user_input = input()
        if user_input == " ":
            score += 1
        elif user_input == "c":
            coins += 1
        else:
            print("Game over! Your score is", score, "and you collected", coins, "coins.")
            return

        obstacles.pop(0)
        obstacles.append(random.choice(["|", " ", "$"]))
        time.sleep(0.1)

game()

























































