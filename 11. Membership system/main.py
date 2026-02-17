username = input("Please enter your username: ")

if len(username) > 12 or " " in username or any(char.isdigit() for char in username):
    print("Incorrect Credentials")
else:
    print(f"Welcome back, {username}!")
    print()

    name = input("Please enter your Full Name: ")
    age = int(input("How old are you?: "))
    gpa = input("GPA: ")
    a_student = bool(input("Are you a student?(True/False): "))
    print()

    print("If you are a student and you are under 25 you have 50% discount!")

    if a_student and age < 25:
        print("You will have a smaller tax to pay, so it will be $25!")
    else:
        print("The tax will be 50$!")

    print()

    print(f"Full Name: {name}")
    print(f"Age: {age}")
    print(f"GPA: {gpa}")
    print(f"Student Status: {a_student}")
    print(f"You have to pay ${50 if a_student == 0 and age < 25 else 25}")
    print(f"{username}@companie.com")
    print()
