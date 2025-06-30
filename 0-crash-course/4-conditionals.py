# python ises indents to define blocks of code

temp = 28
if temp > 30:
  print("it's a hot day")
elif temp < 20:
  print("it's a nice day")
else:
  print("it's a pleasant day")

  # checking multiple conditions with logical operators
age = 25
has_license = True

if age >= 18 and has_license:
    print("you can drive")
elif age < 18 and not has_license:
    print("you can't drive you need to be 18 and have a license")
else:
    print("you can drive but you need a license")

# nested conditionals
score = 85
if score >= 60:
    print("you passed")
    if score >= 90:
        print("excellent")
    elif score >= 80:
        print("good job")
    else:
        print("you did well")
else: 
    print("you failed")
    if score < 50:
        print("you need to retake the exam")
    else:
        print("you can try again next time")


# using the "in" operator with conditionals
fruit = "banana" 
if fruit in ["apple", "banana", "orange"]:
    print(f"{fruit} is a common fruit")       

# ternary operator one line if else
age =20
status = "adult" if age >= 18 else "minor"
print(f" status: {status}")


# comparing strings
password = "secret123"
if password == "secret123":
    print("access granted")
else:
    print("access denied")

# changing comparison
x = 15
if 10 <= x <= 20:
    print("x is between 10 and 20")

 # truthy or falsy value
user_input = ""

if user_input:
    print("you entered something")
else:
    print("you didn't enter anything")
