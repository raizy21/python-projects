print("website checker app")

url = input("\nenter a website url to check: ")

if url.startswith("https://"):
   print("the website is secure (https)")
elif url.startswith("http://"):
    print("the website is not secure (http)") 
else:
    print("the website url is invalid, it should start with http:// or https://")