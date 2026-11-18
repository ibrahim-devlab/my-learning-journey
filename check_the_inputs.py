


import accs_manage

def check_n(n, s):
    not_valid = "not_valid"
    if s == "1":
        choices = ["1", "2", "3"]
        if n in choices:
            return n
        else:
            print(f"wrong choice, choice from the list.")
    elif s == "2":
        choices = ["1", "2", "3"]
        if n in choices:
            return n
        else:
            print(f"wrong choice, choice from the list.")
    elif s == "3":
        if len(n) < 1:
            return not_valid

        numbers_and_dot = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        dot = ["."]
        k = 0
        d = 0
        for i in n:
            if i in numbers_and_dot:
                k += 1
            if i in dot:
                d += 1
        if k != len(n) or d > 1:
            return not_valid

        nf = float(n)
        return nf
    elif s == "4":
        not_enough = "not_enough"
        numbers_and_dot = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        k = 0
        d = 0
        for i in n:
            if i in numbers_and_dot:
                k += 1
            if i in dot:
                d += 1
        if k != len(n) or d > 1:
            return not_valid
        nf = float(n)
        if nf > accs_manage.account["balance"]:
            return not_enough
        return nf