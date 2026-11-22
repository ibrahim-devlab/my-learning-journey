


from datetime import datetime

accs = []
account = {}
count_accs = []
number = 0
def create_acc(nasb, password):
    c_date = datetime.today()
    name = nasb.split(" ")[0]

    global account, number
    number += 1
    account = {"acc_number": number, "acc_nasb": nasb,"acc_name": name, "acc_password": password, "balance": 0.0, "acc_cre_date": str(c_date)}
    accs.append(account)
    count_accs.append(number)

    return account
