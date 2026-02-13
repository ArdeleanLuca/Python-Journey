# The password security system
correct_username = "admin"
correct_password = "python123"
username_user = input("Please introduce your username: ")
password_user = input("Please introduce your password: ")

if len(password_user) < 6:
    print("Error: Password too short!")
elif username_user == correct_username and password_user == correct_password:
    print(f"Access Granted! Welcome, {correct_username}!")
else:
    print("Invalid Credentials.")
