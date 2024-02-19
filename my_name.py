USER_PASSWORD = "LIUSIYI"

min_length = 7

password = input("Please enter your password:")

while len(password) < min_length:
    print("Invalid password, password must be at least 7 characters long.")
    password = input("Please enter your password:")

print("*" * len(password))
