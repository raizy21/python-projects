print("reverse-name-generator")

while True:
    name = input("enter a name to reverse (or type 'exit' to quit): ")
    
    if name.lower() == 'exit':
        print("goodbye!")
        break
    
    reversed_name = name[::-1]
    print(f"reversed name: {reversed_name}")
    print(f"in a parallel universe, your name is: {reversed_name.title()} ")

     