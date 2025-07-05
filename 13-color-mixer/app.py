print("color-mixer")

color_mixer = {
  ("red", "blue"): "purple",
  ("red", "yellow"): "orange",
  ("blue", "yellow"): "green",
  ("blue", "green"): "teal",
  ("red", "green"): "brown",
} 


while True:
  color1 = input("enter first color: ").lower().strip()
  color2 = input("enter second color: ").lower().strip()

  mix = None 

  if (color1, color2) in color_mixer:
    mix = color_mixer[(color1, color2)] 
  elif (color2, color1) in color_mixer:
    mix = color_mixer[(color2, color1)]

  if mix:
    print(f"{color1} + {color2} = {mix}")
  else:
    print(f"sorry, i don't know how to mix {color1} and {color2}.")

  if not input("press enter to continue or type 'exit' to quit: ").lower() != "exit":
    print("goodbye!")
    break