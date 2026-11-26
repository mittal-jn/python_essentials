#print greetings
def greet_user(name1):
   
    if name1 == "" :
        print("Hello! Welcome!")
    else:
        print(f"Hello, {name1}! Welcome!")
name=input("Enter your name:").strip()
greet_user(name)

