# functions are blocks of code that perform a specific task and can be reused
# they can take inputs (arguments) and return outputs (return values)

def greet_everyone():
    print("hello, everyone!")

greet_everyone()

def greet(name):
    print("hello, ",name)

greet("andrei")
greet("john")
greet("jane")

# without functions, we would have to repeat the same code for each user
# this is not efficient and can lead to errors if we need to change the code
user1 = "andrei"
print("hello " , user1 , "welcome to the app!")
print("we hope you enjoy your stay!")
print("let us know if you have any questions or feedback!")



user2 = "razvan"
print("hello " , user2 , "welcome to the app!")
print("we hope you enjoy your stay!")
print("let us know if you have any questions or feedback!")


user3 = "chiper"
print("hello " , user3 , "welcome to the app!")
print("we hope you enjoy your stay!")
print("let us know if you have any questions or feedback!")


# instead, we can use a function to greet each user
# this way, we can reuse the same code for each user and avoid repetition
def greet_user(user):
    print("hello " , user , "welcome to the app!")
    print("we hope you enjoy your stay!")
    print("let us know if you have any questions or feedback!")


greet_user("andrei")
greet_user("razvan")
greet_user("chiper")

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
    

x = power(2,5)  # 32
y = power(3,3)  # 27
z = power(5,2)  # 25

print("2^5 =", x)
print("3^3 =", y) 
print("5^2 =", z)
print(power(5,5))
  
