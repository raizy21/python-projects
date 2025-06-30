# list are collections of items that can store different types of data

numbers = [1, 2, 3, 4, 5]
# print the list
print(numbers)

print(numbers[0])  # Accessing the first item in the list
numbers.append(6)  # Adding an item to the end of the list
numbers[1] = 10  # Changing the second item in the list
# print the modified list 
print(numbers)

numbers.remove(3)  # Removing an item from the list
# print the modified list 
print(numbers)

# length of the list
print(len(numbers))  # Output: 4

# slicing the list
numbers = [1, 2, 3, 4, 5]
print(numbers[1:3])  # Output: [2, 3]
print(numbers[:3])  # Output: [1, 2, 3]
print(numbers[2:])  # Output: [3, 4, 5]
print(numbers[-1])  # Output: 5 (last item in the list)
print(numbers[::-1])  # Output: [5, 4, 3, 2, 1] (reversed list)
print(numbers[::2])  # Output: [1, 3, 5] (every second item)
print(numbers[1:5:2])  # Output: [2, 4] (every second item starting from index 1)
print(numbers + [6, 7])  # Concatenating two lists
print(numbers * 2)  # Repeating the list

# lists can contain different types of data
list_of_items = [1,2,3, "andrei", 4.5, True, None]
# print the list
print(list_of_items)


# dictionaries are collections that store key-value pairs
student = {
    "name": "andrei", 
    "age": 30,
    "courses": ["python", "javascript"],
    "is_active": True,
}

print(student)  # Print the dictionary
print(student["name"])  # Accessing a value by key
student["age"] = 31  # Changing a value by key
print(student["age"])  # Print the updated age
print(student.keys())  # Print all keys in the dictionary
print(student.values())  # Print all values in the dictionary
print(student.items())  # Print all key-value pairs in the dictionary
print("name" in student)  # Check if a key exists in the dictionary

for key, value in student.items():  # Iterating through key-value pairs
    print(f"{key}: {value}")

# sets are unordered collections of unique items - no duplicates allowed
unique_colors = {"red", "green", "blue", "blue"}
print(unique_colors)  # Print the set


# tuples are ordered collections that cannot be changed (immutable) after creation
coordinates = (10.0, 20.0)  # Creating a tuple
print(coordinates)  # Print the tuple
print(coordinates[0])  # Accessing the first item in the tuple
