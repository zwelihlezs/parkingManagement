from malls import malls
from methods.signUp import *
from methods.getUsers import *
from methods.login import *


print('%.2f' % malls[0]['fee'])

users = GetUsers()
# SignUp
currentUser = Login(users)
print(type(currentUser))
print(f'\nusername: {currentUser["username"]} \nRole: {currentUser["role"]}\n')


## MAIN MENU ##

def Menu():
    print('===== Parking Management System =====')
    print()
    currentUser = ''
    loginAttempt = 0
    while currentUser =='' and loginAttempt < 3:
        loginAttempt +=1
        # currentUser = login()

