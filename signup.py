#get user Role for sign up

def GetUserRole():
    userRole = ''
    while userRole != 'customer' or userRole != 'admin' or userRole != 'owner':
        userInput = input('Choose your role (\n1. customer\n 2. admin\n 3. owner\n)\n')

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


#User registration

def SignUp(role):

    #customer register
    def CustomerRegister():
        userername = input('Enter your username: \n')
        password = input('Enter your password')
        role = 'customer'

    # Add customer to external file
    

