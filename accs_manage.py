


counter = 0
accs = []
def create_acc(nasb, password):
    acc = []
    global counter
    counter += 1
    acc.append(counter)      # account number   [0]
    acc.append(nasb)         # account name     [1]
    acc.append(password)     # account password [2]
    acc.append(float(0))     # account balance  [3]

    accs.append(acc)
    acc_info = f"account name: {acc[1]}, account number: {acc[0]}, account balance: {acc[3]}"
    return acc_info

print(create_acc('ibrahim', 4444))
print(create_acc('test', 123))

def get_acc(card):
    
    a = 0
    for i in range(0, len(accs)):
        if card == accs[a][0] or card == accs[a][1]:
            print(f"welcome back {accs[a][1]}")
            acc_gate = accs[a]

        else:
            a += 1
    if a == len(accs):
        print(f"no account found with \"{card}\"")
        

get_acc(3)

