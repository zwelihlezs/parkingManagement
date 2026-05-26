from files.malls import malls

###customer funcions/actions

#choose mall

def chooseMall(user):
    #let user choose a mall and add it to user prof
    print('---- MALL ----')
    chosenMall = int(input(f'1. Gateway Theatre of Shopping \n2. Pavilion Shopping Centre \n3. La Lucia Mall\n'))
    print(malls[chosenMall])
    if chosenMall == '1':
        mall = malls[0]
        user['mall'] = mall

    elif chosenMall == '2':
        mall = malls[1]
        user['mall'] = mall

    elif chosenMall == '3':
        mall = malls[2]
        user['mall'] = mall
#admin function/actions

#owner functions/actions
