#Validate input user exercise

username = input("Please choose a wisely username: ")

if len(username) > 12 or " " in username or any(char.isdigit() for char in username):
    print("Incorrect data")
else:
    print(f"Welcome back {username}")
