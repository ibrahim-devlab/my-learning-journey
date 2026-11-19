



from check_the_inputs import check_n
import accs_manage
from accs_manage import create_acc
import time

n = ""
while n != "3":
    print(f"welcome to probank! choice from the list")
    print(f"1: for entering to your account.")
    print(f"2: for creating a new account.")
    print(f"3: to quiet the app.")

    n = check_n(input(), "1")
    
    if n == "2":
        nasb = input(f"Enter your nasb: ")
        t_nasb = check_n(nasb, "5")
        while t_nasb == "not_valid":
            print(f"the nasb shoubd be at least 2 names each at least 2 charecter with space betwein them!")
            nasb = input(f"enter a valid nasb!: ")
            t_nasb = check_n(nasb, "5")

        password = input(f"create a new 4 digits password: ")
        res = check_n(password, "6")
        while res == "not_valid":
            print(f"invalid password: the password should be only 4 digits!: ")
            password = input(f"enter a valid password: ")
            res = check_n(password, "6")
    
        info = create_acc(nasb, password)
        print(f"the account has been created!")
        print(f" thank you {info["acc_name"]} for choucing probank!")

        time.sleep(3)
        
        n2 = ""
        while n2 != "3":
            print(f"welcome {info["acc_name"]} to your account!")
            print(f"nasb: {info["acc_nasb"]}")
            print(f"balance: {info["balance"]}")
            print(f"account creation date: {info["acc_cre_date"]} \n")

            print(f"choice from the list:")
            print(f"1: deposit")
            print(f"2: withdraw")
            print(f"3: to exit from account menu")

            n2 = check_n(input(), "2")
            
            if n2 == "1":

                print(f"enter the amount: ")
                dep_amo = check_n(input(), "3")

                while dep_amo == "not_valid":
                    print(f"enter a valid value, only digits and dot \".\"")
                    dep_amo = check_n(input(), "3")

                accs_manage.account["balance"] += dep_amo
            elif n2 == "2":
                print(f"enter the amount: ")
                wit_amo = check_n(input(), "4")
                
                while wit_amo == "not_valid" or wit_amo == "not_enough":
                    if wit_amo == "not_valid":
                        print(f"enter a valid value, only digits and dot \".\"")
                    elif wit_amo == "not_enough":
                        break
                    wit_amo = check_n(input(), "4")
                
                if wit_amo == "not_enough":
                    print(f"you dont have enough in your account!")
                else:
                    accs_manage.account["balance"] -= wit_amo
