import json
from methods.getUsers import GetUsers

#get all users from external file
users = GetUsers()

def Login(users): 

    currentUser = {}

    print('########## Login ###########')
    username = input('username: ')
    password = input('password: ')

    for user in users:
        if username == user['username'] and password == user['password']:
            currentUser = user
            login = 'successful'
            print('Login SuCcEsSfUl')
        else:
            login = 'failed'
    return currentUser


        
        