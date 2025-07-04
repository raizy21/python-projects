import random

print("random recipe generator")

proteins = ["chicken", "beef", "tofu", "fish"]
veggies = ["broccoli", "carrots", "spinach", "bell peppers"]
carbs = ["rice", "pasta", "quinoa", "bread"]
methods = ["grilled", "stir-fried", "baked", "steamed"]
flavors = ["spicy", "sweet", "savory", "herb-infused"]

while True:
    print("\ngenerating a random recipe...")
    
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(f"\nyour random recipe is: {flavor} {method} {protein} with {veggie} and {carb}.")
    
    if input("do you want to generate another recipe? (yes/no): ").lower() != "yes":
        print("thanks for using the random recipe generator!")
        break     
