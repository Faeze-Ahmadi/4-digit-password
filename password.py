password = [int(i) for i in input("Enter the 4-digit password: ")]

def password_restrictions(num):
    if len(password) == 4:
        if password[2] / password[0] == 4:
            if password[-1] % 2 != 0:
                return password

print(password_restrictions(password))