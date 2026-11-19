


import re
import accs_manage

def check_n(n, s):
    not_valid = "not_valid"
    not_enough = "not_enough"
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
        match = re.fullmatch(r'(?:[1-9]\d*(?:\.\d+)?|0\.\d+)', n)
        if match:
            nf = float(n)
            return nf
        else:
            return not_valid
    elif s == "4":
        match = re.fullmatch(r'(?:[1-9]\d*(?:\.\d+)?|0\.\d+)', n)
        if match:
            nf = float(n)
            if nf > accs_manage.account["balance"]:
                return not_enough
            return nf
        else:
            return not_valid
    elif s == "5":
        match = re.fullmatch(r'(?:[a-z A-Z]{2,}\s[a-z A-Z]{2,})', n)
        if match:
            return n
        else:
            return not_valid
    elif s == "6":
        match = re.fullmatch(r'[\d]{4}', n)
        if match:
            return n
        else:
            return not_valid