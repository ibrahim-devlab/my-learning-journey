



from accs_manage import get_acc
from password_check import passcheck
i = 1
while (i < 2):

    try:
        inpu = int(input("enter 1 to get to your account, enter 2 to create an account.: "))
        if inpu == 1 or inpu == 2:
            i += 1
    except ValueError:
        print("enter a correct value")

if inpu == 2:
    acc_nasb = input("enter your nasb: ")
    
    password = (input("enter a 4 digits password: "))
    pas = passcheck(password)
    if pas == 0:
        print("invalid password: the password should be only 4 digits!.")
        
else:
    card = input("Enter your name or your account number: ")
    print(get_acc(card))