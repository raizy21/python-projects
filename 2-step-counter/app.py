print("step counter app")

daily_goal = int(input("\nenter your daily step goal: "))
current_steps = int(input("enter your current step count: "))

remaining_steps = daily_goal - current_steps

if remaining_steps > 0:
    print(f"\nyou need {remaining_steps} more steps to reach your daily goal of {daily_goal} steps.")
else:
    print(f"\nyou have reached your daily goal of {-remaining_steps} steps!")