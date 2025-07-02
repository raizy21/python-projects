print('character type checker app')

char = input("enter a single character: ")

if char.isalpha():
    print("the character is an alphabet letter.")
elif char.isdigit():
    print("the character is a digit.")
elif char.isspace():
    print("the character is a whitespace.")
else: 
    print("the character is a special character or punctuation mark.")