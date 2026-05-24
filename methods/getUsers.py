import json

# get all user

def GetUsers():
    #users = ''

    with open('files/users.json', 'r') as file:
        users = json.load(file)

    return users

def DisplayUsers(users):
    for user in users:
        print(f'\nUsername: {user['username']}')
        print(f'\nUser Role: {user['role']}')
        print('_______________________________________')

# get customers
def GetCustomers(users):
    customers = []

    for user in users:
        if user['role'] == 'customer':
            customers.append(user)
    return customers

# get admins

def GetAdmin(users):
    administrators = []

    for user in users:
        if user['role'] == 'admin':
            administrators.append(user)
    return administrators

# get owners

def GetOwners(users):
    owners = []

    for user in users:
        if user['role'] == 'owner':
            owners.append(user)
    return owners
