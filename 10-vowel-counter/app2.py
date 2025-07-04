print("vowel counter")

while True:
    text = input("enter text (or type 'exit' to quit): ")
    if text.lower() == "exit":
        print("exiting the program.")
        break


    vowels = sum(1 for char in text.lower() if char in 'aeiou')
    print(f"the number of vowels in the text is: {vowels}")