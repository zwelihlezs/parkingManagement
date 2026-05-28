from files.malls import malls
import datetime

###customer funcions/actions

#choose mall

def CustomerMenu():
    
    
    choice = input('Choice: ')
    return choice

def chooseMall(user):
    #let user choose a mall and add it to user prof
    print('---- MALL ----')
    chosenMall = int(input(f'1. Gateway Theatre of Shopping \n2. Pavilion Shopping Centre \n3. La Lucia Mall\n'))
    
    if chosenMall == '1':
        mall = malls[0]
        user['mall'] = mall

    elif chosenMall == '2':
        mall = malls[1]
        user['mall'] = mall

    elif chosenMall == '3':
        mall = malls[2]
        user['mall'] = mall



def displayFees(user):
    print(f'Fees:R{user['fees']}')

def payFees(user):
    if user['fees'] > 0:
        print(f'Outstanding fees: R{user['fees']}\n')
        action = input('Choose what to do: \n1. Pay outstanding fess. \n2. pay later(Exit)\n')
        if action == '1':
            print('\npayment SuCcEsSfUl... :)')
        elif action == '2':
            print('Bye')

def CustomerMenu(user):
    print('#### Customer Menu ####')
    print('Select a mall')
    
    mallChoice = input('1. Gateway Theatre of Shopping \n2. Pavilion Shopping Centre \n3.La Lucia Mall')
    
    if mallChoice == '1':
        currentMall = user['mall1']
    if mallChoice == '2':
        currentMall = user['mall2']
    if mallChoice == '3':
        currentMall = user['mall3']

    userinput = input('1. Vehicle entry \n2. Vehicle exit \n3.View History \n4. Pay Outstanding fees \n5. Logout')


#admin function/actions

def registerVehicleEntry(user):
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    userEntry = [user['name'], '|', time]
    return userEntry


#owner functions/actions
