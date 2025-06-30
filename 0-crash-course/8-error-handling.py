try: 
  number = int(input("enter a number: "))
  result = 10 / number
  print(f"10 divided by {number} is {result}")

except ValueError:
  print("invalid input. please enter a valid number.")

except ZeroDivisionError:
  print("error: division by zero is not allowed.")
  print("please enter a non-zero number.")
finally:
  print("this will always execute, regardless of whether an error occurred or not.")
