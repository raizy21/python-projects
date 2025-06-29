import  math
# basic arithmetic operations
x = 10
y= 5

print ("x =", x)
print ("y =", y)

print ("x + y =", x + y)
print ("x - y =", x - y)
print ("x * y =", x * y)
print ("x / y =", x / y)
print ("x % y =", x % y)
print ("x ** y =", x ** y)
print ("x // y =", x // y)
print ("x < y =", x < y)  
print ("x > y =", x > y)
print ("x <= y =", x <= y)
print ("x >= y =", x >= y)
print ("x == y =", x == y)

x += 5
print ("x after incrementing by 5:", x)
x -= 3
print ("x after decrementing by 3:", x)


# string concatenation
first_name = "andrei"
last_name = "razvan"

full_name = first_name + " " + last_name
print ("full name:", full_name)

print("hey my name is", full_name)

# f strings
print(f"hey my name is {full_name}")


# int floor division
a=17
b=5
print("a / b =", a / b)  # results in 3.4, the float division
print("a // b =", a // b) # results in 3, the integer part of the division

# assign multiple variables
i, j, k= 1, 2, 3
print("i, j, k =", i, j, k)  # prints the values of i, j, k

# swapping values
m = 10
n = 20
print("Before swapping: m =", m, ", n =", n)
m, n = n, m  # swap values
print("After swapping: m =", m, ", n =", n)

# comparison operators
c = 5
d = 10

print("c =", c, ", d =", d)

print(c == d)  # prints False, since 5 is not equal to 10
print(c != d)  # prints True, since 5 is not equal to 10
print(c < d)   # prints True, since 5 is less than 10
print(c > d)   # prints False, since 5 is not greater than 10
print(c <= d)  # prints True, since 5 is less than or equal to 10
print(c >= d)  # prints False, since 5 is not greater than or equal

# logical operators
a = True
b = False

print("a and b =", a and b)  # prints False, since one of the operands is False
print("a or b =", a or b)    # prints True, since one of the operands is True
print("not a =", not a)      # prints False, since a is True
print("not b =", not b)      # prints True, since b is False

# string slicing
text = "python programming"
print(text[0:6])  # prints "python"
print(text[7:18]) # prints "programming"
print(text[:6])    # prints "python"
print(text[7:])    # prints "programming"
print(text[::-1]) # prints "gnimmargorp nohtyp", reversing the string

# string formatting
name = "andrei"
age = 30
msg = f"my name is {name} and i am {age} years old."
print(msg)  # prints "my name is andrei and i am 30 years old."

# using placeholders
msg2 = "my name is {0} and i am {1} years old. {0} is a nice name.".format(name, age)
print(msg2)  # prints "my name is andrei and i am 30 years old. andrei is a nice name."

#math module operations
print(math.sqrt(16))  # prints 4.0, the square root of 16
print(math.pow(2, 3))  # prints 8.0, 2 raised to the power of 3
print(math.pi)        # prints 3.141592653589793, the value of
print(math.e)         # prints 2.718281828459045, the value of e
print(math.factorial(5))  # prints 120, the factorial of 5
print(math.gcd(12, 15))  # prints 3, the greatest common divisor of 12 and 15

pi = 3.13159
print(f"pi rounded to 2 decimal places: {pi:.2f}")  # prints "pi rounded to 2 decimal places: 3.13"
print(f"pi rounded to 3 decimal places: {pi:.3f}")  #