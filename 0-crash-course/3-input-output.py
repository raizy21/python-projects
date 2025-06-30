# simple input and output example
name = input("what is your name? ")
print("hello, " + name + "!")


# simple input and output example with age calculation
age = input("how old are you? ")
years_to_100 = 100 - int(age)
print("you will be 100 years old in " + str(years_to_100) + " years.")


# sum result float numbers
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
sum_result = num1 + num2
print(f"the sum of {num1} and {num2} is: {sum_result}")

# working with multiple inputs
x,  y = input("enter two numbers separated by a space: ").split()
print(f"first number: {x}, second number: {y}")

# chose a color with default value
user_choice = input("choose a color or press enter for default: ")
if user_choice == "":
    user_choice = "blue"
print(f"selected color: {user_choice}")

# possibility are endless
length = float(input("enter the length in meter: "))
print(f"the length in meter is: {length* 100} cm")