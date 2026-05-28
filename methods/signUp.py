import json
from files.malls import malls
from pathlib import Path

##User sign up
def GetUserRole():
    userRole = ''
    while userRole != 'customer' or userRole != 'admin' or userRole != 'owner':
        userInput = input('Choose your role (\n 1. customer\n 2. admin\n 3. owner\n)\n')

        if userInput == '1':
            userRole = 'customer'
            break
        elif userInput == '2':
            userRole = 'admin'
            break
        elif userInput == '3':
            userRole = 'owner'
            break
        else:
            print('Please enter correct ROLE')

        print('re: '+userInput +' as: ' +userRole)
        print()
    return userRole

#get user's list from external file
def GetUsers():
        path = Path('files/users.json')
        if path.exists() and path.stat().st_size > 0:
            with open('files/users.json', 'r') as file:
                 users = json.load(file)
                 return users
        else:
             users = []
             print('empty')
             return users

        print(f'get users: {users}')
        



def SignUp():
    #user sign up and create prof
    users = GetUsers()
    print(type(users))
    print(f'user: {users}')
    username = ''
    password = ''

    while username == '' and password == '':
        print('########### Sign Up #############')
        username = input('\nEnter your username: ')
        password = input('\nEnter your password: ')
        role = GetUserRole()

    if role == 'customer':
        user = {
            "username": username,
            "password": password,
            "role": role,
            "mall1": [{'mall':malls[0]["name"]},{'fees': 0},{'visits': 0}],
            "mall2": [{'mall':malls[1]["name"]},{'fees': 0},{'visits': 0}],
            "mall3": [{'mall':malls[2]["name"]},{'fees': 0},{'visits': 0}]
    }
    
    # users = list(users)
    users.append(user)
    print(f'appended: {users}')
    #save user login's to external file
    
    with open('files/users.json', 'w') as file:
            json.dump(users, file, indent=4)
        
    print(user)


#get customer's list from external file

#get administrators' list from external file

#get users' list from external file



