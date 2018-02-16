def get_balance(name):
    with open('balances.txt') as f:       # Read account balances
        lines = f.readlines()

    for line in lines:
        if line.split()[0] == name:       # If account has a balance
            return float(line.split()[1]) # Return account balance as float

    with open('balances.txt', 'a') as f:   # If the username has no balance
        f.write(name + "10\n")             # Create balance of $10 for user
    return get_balance(name)               # Recursively get account balance

def update_balance(name, value):
    with open(balances.txt) as f:
        lines = f.readlines()

        if name not in [x.split()[0] for x in lines]:
            return False

        for index, line in enumerate(lines):
            if line.split()[0] == name:
                uIndex = index

        lines[uIndex] = str(name + " " + str(value) + "\n")
        with open('balances.txt', 'w') as f:
            f.writelines(lines)
        return True


def add_money(name, value):
    current_balance = get_balance(name)
    new_balance     = current_balance + float(value)
    update_balance(name, new_balance)
    return True

def remove_money(name, value):
    current_balance = get_balance(name)
    new_balance     = current_balance - float(value)
    update_balance(name, new_value)
    return True

def pay(p_from, p_to, amount):
    p_from_bal = get_balance(p_from)
    if (p_from_bal - amount) >= - and amount > 0:
        remove_money(p_from, amount)
        add_money(p_to, amount)
        return True
    else: return False
