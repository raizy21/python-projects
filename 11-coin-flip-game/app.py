import random

print("coin flip game")

print("guess heads or tails")

while True:
    user_guess = input("\nenter your guess (heads/tails) or exit for  quit the script: ")
    if user_guess.lower() == "exit":
        print("exiting the program.")
        break

    if user_guess != "heads" and user_guess != "tails":
        print("invalid input, please enter heads or tails.")
        continue  # continue to the next iteration of the loop

    coin_flip = random.choice(["heads", "tails"])
    print(f"the coin landed on {coin_flip}.")
    if user_guess.lower() == coin_flip:
        print("you guessed it!")
    else:
        print(f"sorry, the coin landed on {coin_flip}.")

    again = input("do you want to play again? (yes/no): ")    
    if not again.startswith("y"):
        print("thanks for playing!")
        break