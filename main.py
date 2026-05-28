from files.malls import malls
from methods.pms import chooseMall
from methods.signUp import *
from methods.getUsers import *
from methods.login import *


print('%.2f' % malls[0]['fee'])

users = GetUsers()
# SignUp
currentUser = Login(users)
chooseMall(currentUser)
# print(type(currentUser))
# print(f'\nusername: {currentUser["username"]} \nRole: {currentUser["role"]}\n')


## MAIN MENU ##

def Menu():
    print('===== Parking Management System =====')
    print()
    currentUser = ''

    #display menu and get user choice
    print('######## MENU ########')
    print('1. Login \n2. Register \n3. Exit')

    userInput = input('Choose an option(1-3): ')
    if userInput == '1':
        currentUser = Login()
    elif userInput == '2':
        SignUp()
        print('Registration successful')
    elif userInput == '3':
        print('Bye')
    else:
        print('Please make sure your input is coorect')

    # if currentUser != '':
        #customerMenu()


