from files.malls import malls
from methods.pms import *
from methods.signUp import *
from methods.getUsers import *
from methods.login import *


#print('%.2f' % malls[0]['fee'])

users = GetUsers()

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
        currentUser = Login(users)
        CustomerMenu()
    elif userInput == '2':
        SignUp()
        print('Registration successful')
    elif userInput == '3':
        print('Bye')
    else:
        print('Please make sure your input is correct')

    if currentUser == '':
        exit




Menu()