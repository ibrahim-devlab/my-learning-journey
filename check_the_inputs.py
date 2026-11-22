


import re
import accs_manage
def check_n(n, s):
    not_valid = "not_valid"
    not_enough = "not_enough"
    if s == "1":
        match = re.fullmatch(r'[1-3]{1}', n)
        if match:
            return n
        else:
            print(f"wrong choice, choice from the list.")
    elif s == "2":
        match = re.fullmatch(r'[1-3]{1}', n)
        if match:
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
            n = int(n)
            return n
        else:
            return not_valid
    elif s == "7":
        if n < 10:
            n = str(n)
            days = {"1": "Monday", "2": "Tuesday", "3": "Wednesday"
            , "4": "Thursday", "5": "Friday", "6": "Saturday", "7": "Sunday"}
            return days[n]
        elif n > 50:
            n -= 50
            n = str(n)
            hours = {"1": "1 AM", "2": "2 AM", "3": "3 AM", "4": "4 AM"
            , "5": "5 AM", "6": "6 AM", "7": "7 AM", "8": "8 AM", "9": "9 AM", "10": "10 AM"
            , "11": "11 AM", "12": "12 PM", "13": "1 PM", "14": "2 PM", "15": "3 PM"
            , "16": "4 PM", "17": "5 PM", "18": "6 PM", "19": "7", "20": "8 PM", "21": "9 PM"
            , "22": "10 PM", "23": "11 PM", "00": "12 AM"}
            return hours[n]
        else:
            n -= 10
            n = str(n)
            months = {"1": "January", "2": "February", "3": "March"
            , "4": "April", "5": "May", "6": "June", "7": "July", "8": "August"
            , "9": "September", "10": "October", "11": "November", "12": "December"}
            return months[n]
    elif s == "8":
        match = re.fullmatch(r'[\d]+', n)
        
        if match:
            n = int(n)
            if n in accs_manage.count_accs:
                return n
            else:
                return not_enough
        else:
            return not_valid
    elif s == "9":
        nnn = n.split(">>>")
        nn = int(nnn[1])
        nn -= 1
        match = re.fullmatch(r'[\d]{4}', nnn[0])
        if match:
            n = int(nnn[0])
            if n == accs_manage.accs[nn]["acc_password"]:
                return n
            else:
                return not_enough
        else:
            return not_valid