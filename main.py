


import datetime
import time
from check_the_inputs import check_n
import accs_manage
from accs_manage import create_acc
c_acc = 0
n = ""
while n != "3":
    print(f"welcome to probank! choice from the list")
    print(f"1: for entering to your account.")
    print(f"2: for creating a new account.")
    print(f"3: to quiet the app.")

    n = check_n(input(), "1")
    
    if n == "2":
        nasb = check_n(input(f"Enter your nasb: "), "5")
        while nasb == "not_valid":
            print(f"the nasb shoubd be at least 2 names each at least 2 charecter with space betwein them!")
            nasb = check_n(input(f"enter a valid nasb!: "), "5")

        password = check_n(input(f"create a new 4 digits password: "), "6")
        while password == "not_valid":
            print(f"invalid password: the password should be only 4 digits!: ")
            password = check_n(input(f"enter a valid password: "), "6")
    
        info = create_acc(nasb, int(password))
        print(f"the account has been created!")
        print(f" thank you {info["acc_name"]} for choucing probank!")

        time.sleep(3)
        
        n2 = ""
        while n2 != "3":
            print(f"welcome {info["acc_name"]} to your account!")
            print(f"account number is {info["acc_number"]}")
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
                d_dep_amo = datetime.datetime.now()
                print(f"{dep_amo} riyals were deposited into your bank account on {check_n(d_dep_amo.isoweekday(), "7")}, {check_n(d_dep_amo.month + 10, "7")} {d_dep_amo.day}, {d_dep_amo.year}, at {check_n(d_dep_amo.hour + 50, "7")}.")
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
                    w_dep_amo = datetime.datetime.now()
                    print(f"{wit_amo} riyals was deducted from your bank account on {check_n(w_dep_amo.isoweekday(), "7")}, {check_n(w_dep_amo.month + 10, "7")} {w_dep_amo.day}, {w_dep_amo.year}, at {check_n(w_dep_amo.hour + 50, "7")}.")
                    accs_manage.account["balance"] -= wit_amo
    if n == "1":
        n_acc = check_n(input(f"enter the account number: "), "8")
        
        while n_acc == "not_valid" or n_acc == "not_enough":
            if n_acc == "not_valid":
                print(f"enter a valid value")
            elif n_acc == "not_enough":
                print(f"no account found, enter a coutect number!")
            n_acc = check_n(input(f"enter the account number: "), "8")

        password = check_n((input(f"enter the account password: "))+">>>"+str(n_acc), "9")
        while password == "not_valid" or password == "not_enough":
            if password == "not_valid":
                print(f"enter a valid password: ")
            elif password == "not_enough":
                print(f"uncoorect password!")
            password = check_n(input(f"enter the account password: ") +">>>"+ str(n_acc), "9")

        while n2 != "3":
            print(f"welcome {accs_manage.accs[n_acc]["acc_name"]} to your account!")
            print(f"account number is {accs_manage.accs[n_acc]["acc_number"]}")
            print(f"nasb: {accs_manage.accs[n_acc]["acc_nasb"]}")
            print(f"balance: {accs_manage.accs[n_acc]["balance"]}")
            print(f"account creation date: {accs_manage.accs[n_acc]["acc_cre_date"]} \n")

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
                d_dep_amo = datetime.datetime.now()
                print(f"{dep_amo} riyals were deposited into your bank account on {check_n(d_dep_amo.isoweekday(), "7")}, {check_n(d_dep_amo.month + 10, "7")} {d_dep_amo.day}, {d_dep_amo.year}, at {check_n(d_dep_amo.hour + 50, "7")}.")
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
                    w_dep_amo = datetime.datetime.now()
                    print(f"{wit_amo} riyals was deducted from your bank account on {check_n(w_dep_amo.isoweekday(), "7")}, {check_n(w_dep_amo.month + 10, "7")} {w_dep_amo.day}, {w_dep_amo.year}, at {check_n(w_dep_amo.hour + 50, "7")}.")
                    accs_manage.account["balance"] -= wit_amo

        
