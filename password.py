# find a number with input for correct password

password = [int(i) for i in input("Enter the 4-digit password: ")]

def password_restrictions(num):
        if len(password) == 4:
            if password[2] / password[0] == 4:
                if password[-1] % 2 != 0:
                    if password[0] - 2 < password[-1] < password[0]:
                        if password[0] == password[1] - 3:
                            if password[1] / password[0] == 2.5:
                                return password

print(password_restrictions(password))

# fond multiple correct passwords in a numeric range