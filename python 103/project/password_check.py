


def passcheck(password):
    result = 0
    if len(password) != 4:
        return result

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    k = 0
    lipassword = []
    for i in password:
        if i in numbers:
            k += 1
    if k != 4:
        return result
    return password
print(passcheck("0125"))

