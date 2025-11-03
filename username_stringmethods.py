# validate user input exercises
# 1. username is no more than 12 characters
# 2. username cannot contain spaces
# 3. username cannot contain digits

username = input("Enter a username: ")

if len(username)>12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username cannot contain digits")
else:
    print(f"Welcome {username}")
    print("Have a good day!")