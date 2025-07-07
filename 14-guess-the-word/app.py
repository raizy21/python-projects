import random

print("guess-the-word")
print("unscramble the letters to find the word!")

words = ["python", "java", "javascript", "coding", "programming", "developer", "software", "algorithm"]


while True:
  original_word = random.choice(words)
  letters = list(original_word)
  random.shuffle(letters)
  scrambled = "".join(letters)

  print(f"scrambled word: {scrambled}")
  guess = input("your guess: ").lower().strip()
  if guess == original_word:
      print("correct! you guessed the word!")
  else:
      print(f"wrong! the correct word was: {original_word}")

  again = input("do you want to play again? (yes/no): ")
  if not again.startswith("y"):
    print("goodbye!") 
    break
