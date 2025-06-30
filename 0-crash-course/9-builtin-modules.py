import random
import math
import datetime
import os
import sys
import time

# get a random number between 1 and 10
random_number = random.randint(1, 10) # 1 and 10 inclusive
print(f"random number between 1 and 10: {random_number}")

# get a random element from a list of fruits
fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print(f"random fruit from the list: {random_fruit}")

# shuffle the list of fruits
random.shuffle(fruits)
print(f"shuffled list of fruits: {fruits}")


# math module examples
print(f"square root of 16: {math.sqrt(16)}")  # Square root
print(f"2 raised to the power of 3: {math.pow(2, 3)}")  # Power
print(f"pi: {math.pi}")  # Value of pi
print(f"e: {math.e}")  # Value of e
print(f"cosine of 0 radians: {math.cos(0)}")  # Cosine
print(f"sine of 0 radians: {math.sin(0)}")  # Sine
print(f"ceiling of 4.2: {math.ceil(4.2)}")  # Ceiling
print(f"floor of 4.8: {math.floor(4.8)}")  # Floor
print(f"factorial of 5: {math.factorial(5)}")  # Factorial


# datetime module examples
current_time = datetime.datetime.now()
print(f"current date and time: {current_time}")
print(f"current date: {current_time.date()}")  # Current date
print(f"current time: {current_time.time()}")  # Current time
print(f"current year: {current_time.year}")  # Current year
print(f"current month: {current_time.month}")  # Current month
print(f"current day: {current_time.day}")  # Current day
print(f"current hour: {current_time.hour}")  # Current hour
print(f"current minute: {current_time.minute}")  # Current minute
print(f"current second: {current_time.second}")  # Current second


# os module examples
current_directory = os.getcwd()
print(f"current working directory: {current_directory}")
print(f"list of files in the current directory: {os.listdir('.')}")


# time module examples
print("waiting for 2 seconds...")
time.sleep(2)
print("done waiting!")

# sys module examples
print(f"python version: {sys.version}")
print(f"platform: {sys.platform}")  # current platform