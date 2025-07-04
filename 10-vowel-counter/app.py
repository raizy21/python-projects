print('vowel counter')

while True:
    text = input('enter text (or type "exit" to quit): ')
    if text.lower() == 'exit':
        print('exiting the program.')
        break

    vowels_cont = 0

    for char in text.lower():
        if char in {'a', 'e', 'i', 'o', 'u'}:
            vowels_cont += 1

    print(f'the number of vowels in the text is: {vowels_cont}')
