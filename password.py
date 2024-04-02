password = [int(i) for i in input("Enter the 4-digit password: ")]

def password_restrictions(num):
    if len(password) == 4:
        return False
    
    