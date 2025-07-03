import random

first_parts = ["Sky", "Star", "Moon", "Sun", "Cloud", "Rain", "Wind", "Fire", "Earth", "Water"]
last_parts = ["Walker", "Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris"]

print("fantasy name generator" )


count = input("how many names do you want to generate? ")

for _ in range(int(count)):
    first = random.choice(first_parts)
    last = random.choice(last_parts)
    print(f"{first}{last}")