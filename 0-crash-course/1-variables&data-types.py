print("hello, world!")

# strings
name = "andrei"
# integers whole numbers
age = 30
# floats decimal numbers
height = 1.8
# booleans true or false
is_student = False


print("hey my name is " + name)
print("i am " + str(age) + " years old.")
print("my height is " + str(height) + " meters.")
print("am i a student? " + str(is_student))


print(name[0])
print(name[0:3])  # slicing
print(name[-1])  # last character

message = "hello world"
print(message.upper())  # uppercase
print(message.lower())  # lowercase
print(message.capitalize())  # title case
print(message.replace("e", "a"))  # replace character
print(message.find("l"))  # find character
print(message.count("l"))  # count character
print(message + " world")  # concatenate strings
print(message * 3)  # repeat string
print("World" in message)  # check if substring exists
print("Hello" not in message)  # check if substring does not exist

greeting1 = "hello"
greeting2 = "Hello"

if greeting1 == greeting2:
    print("greetings are the same")
else:
    print("greetings are different")


# type conversion


age_str = "30"
age = int(age_str)  # convert string to integer 
print(type(age_str))  # check type
print(type(age))  # check type after conversion

price_float = 19.99
price_str = str(price_float)  # convert float to string
price_int = int(price_float)  # convert float to integer

print(price_str)  # print string representation
print(price_int)  # print integer representation
# type checking
print(type(price_float))  # check type of float
print(type(price_str))  # check type of string
print(type(price_int))  # check type of integer