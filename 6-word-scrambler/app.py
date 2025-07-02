import random

print("word-scrambler")

while True:
    word = input("enter a word (or 'exit' to quit): ")
    if word.lower() == 'exit':
        print("exiting the program.")
        break


# "everyone"  ["e", "v", "e", "r", "y", "o", "n", "e"]
# shuffled    ["e", "n", "e", "o", "v", "r", "y", "e"]
    letters = list(word)
    random.shuffle(letters)
    print(f"scrambled word: {''.join(letters)}")
    