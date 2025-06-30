# for loop 
print("continue from 0 to 5:")
for i in range(1,6):
    print(i)


# reverse counting from 5 to 1
print("\nreverse counting from 5 to 1:")
for i in range(5,0,-1):
    print(i)

# wile loop
count = 1
print("\ncounting from 1 to 5 using while loop:")
while count <= 5:
    print(count)
    count += 1

 # reverse wile loop
count = 5
print("\ncounting from 5 to 1 using while loop:")
while count >= 1:
    print(count)
    count -= 1


# looping through a list
fruits = ["apple", "banana", "cherry"]
print("\nlooping through a list of fruits:")
for fruit in fruits:
    print(fruit)

# reversing a list
print("\nreversing a list of fruits:")
for fruit in reversed(fruits):
    print(fruit)

# loop with enumerate
print("\nlooping through a list with index:")
for index, fruit in enumerate(fruits):
    print(f"index: {index}, fruit: {fruit}")

# loops with dictionary
person = {"name": "andrei", "age": 30, "city": "hildesheim"}
print("\nlooping through a dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# list comprehension compact loop for creating lists
squared_numbers = [x**2 for x in range(1, 6)] # 1,4,9,16,25
print("\nsquared numbers from 1 to 5 using list comprehension:")
print(squared_numbers)  

# fruits = ["apple", "banana", "cherry"]
#for loop with zip()
colors = ["red", "yellow", "blue"]

print("\nfruits and theier colors:")
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")

# break and continue in loops
print("\nusing break and continue in loops:")

for i in range(1, 10):
    if i > 5:
        break
    print(i)

# continue in loops
print("\nusing continue in loops:")
for i in range(1, 10):
    if i == 3:
        continue # skip the number 3
    print(i)

# infinite loops with break condition
print("\ninfinite loop with break condition:")
i =1
while True:
    print(i)
    if i >= 5:
        break # exit the loop when i is greater than or equal to 5
    i += 1