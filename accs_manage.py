


from datetime import datetime

accs = []
account = {}

def create_acc(nasb, password):
    c_date = datetime.today()
    name = nasb.split(" ")[0]

    global account
    account = {"acc_nasb": nasb,"acc_name": name, "acc_password": password, "balance": 0.0, "acc_cre_date": str(c_date)}
    accs.append(account)

    #print(accs, account, name, c_date)

    return account
