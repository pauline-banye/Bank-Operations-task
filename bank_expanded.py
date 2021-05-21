
import os
import random
import re
import datetime


user_recs = "data/user_records/"


#validation
def genaccnum():
    print( "" )
    return str(random.randrange(1, 10**10))

def valid_phonenum():
    while True:
        phonenum = input('\nEnter your phone number : ')
        if len( phonenum ) != 11 or not str( phonenum.isdigit() ):
            print("Phone number must be 11 digits, try again")
            phonenum == False
        else:
            return str(phonenum)

def valid_accnum():
    while True:
        accountnum = input('\nEnter the Account Number : ')
        if len( accountnum() != 10 ) or not ( accountnum.isdigit() ):
            print( "Account number must be 11 digits, try again" )
            accountnum == False
        else:
            return True

def valid_email():
    symb = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    while True:
        email = input('\nEnter your email : ')
        if not re.match( symb, email ):
            print('invalid email')
            email == False
        else:
            return email

def validpassword():
    print( "" )
    symbols = "!@#$%^&*()-+?_=,<>/"
    while True:
        password = input( "Create your password : " )
        if not any( c in symbols for c in password ):
            print( "Password must contain special character" )
        elif len( password ) < 8:
            print( "Password is too short" )
        elif not any( password.isupper() for password in password ):
            print( "Password must contain at least one uppercase letter" )
        elif not any( password.islower() for password in password ):
            print( "Password must contain at least one lowercase letter" )
        elif not any( password.isdigit() for password in password ):
            print( "Password must contain at least one number" )
        else:
            return password



#user records creation and authentication
def create_account():
    print("\n\n========== NEW USER REGISTRATION ========== \n\n")

    firstname = input('\nEnter your firstname : ')

    surname = input('\nEnter your surname : ')

    email_addy = valid_email()
    
    phonenum = str(valid_phonenum())

    accpassword = validpassword()

    accountnum = genaccnum()

    amount = 0

    user_data = ([str(accountnum) +","+ firstname +","+ surname +","+ email_addy +"," + str(phonenum) +"," + accpassword +","+ str(amount)])
   
    #print(user_data)
    create_data(accountnum, user_data)

    print("====== ACCOUNT CREATED ======  \n")
    print("Your new account number is %s" % accountnum)

    next = ('\nWould you like to log into your new account? \n    YES [1] : NO [2]:  ')

    if (next == 1):
        login()
    elif (next == 2):
        logout()
    else:
        print("invalid option selected, try again \n")

def create_data(accountnum, user_data):
    
    if find_account_rec(accountnum):
        return False

    try:
        with open(user_recs + str(accountnum) + ".txt", "w") as f:
            f.write(str(user_data))

    except FileExistsError:
        have_data = read_account_rec(user_recs + str(accountnum) + ".txt")
        if not have_data:
            delete(user_data)
        print ('User already exists')

def find_account_rec(accountnum):
    users = os.listdir( user_recs )

    for user in users:
        if user == str( accountnum ) + ".txt":
            #print(accountnum)
            return True

    return False

def read_account_rec(accountnum):
    users = os.listdir( user_recs )

    for user in users:
        
        try:
            if user == str(accountnum) + ".txt":
           
                with open( user_recs + str( accountnum ) + ".txt", "r" ) as f:
                    print('')
                    #print (f.readline())
                    print (f.read())
               
            else:
                with open( user_recs + str(accountnum), "r" ) as f:
                    print('not allowed')
                    return False
        
        except FileNotFoundError:
            print( "User not found" )
    
        #finally:
        #    f.close()

def delete(user_data):
    deleted = False

    if os.path.exists( user_recs + str( user_data ) + ".txt" ):
        try:
            os.remove( user_recs + str( user_data ) + ".txt" )
            deleted = True
        except FileExistsError:
            print( "User Exists already" )

        finally:
            return deleted

def find_password(accountnum):
    find_account_rec(accountnum)
           
    try:
        with open( user_recs + str( accountnum ) + ".txt", "r" ) as f:
                    
            fields = f.read().split(',')

            accountnum = fields[0]
            firstname = fields[1]
            surname = fields[2]
            email_addy = fields[3]
            phonenum = fields[4]
            accpassword = fields[5]
            amount = fields[6]

            if accpassword in fields:
                print(accpassword)
            else:
                print('password not found')
        
    except FileNotFoundError:
        print( "User not found" )

def legit_password():
    legit_password = accpassword

def legit_account():
    legit_account = accountnum

def legit_user(legit_account, legit_password):   
    legit_account = input('\nEnter your Account number: ')
    users = os.listdir( user_recs )

    for user in users:
        if user == str( legit_account ) + ".txt":
            try:
                with open( user_recs + str( legit_account ) + ".txt", "r" ) as f:
                            
                    fields = f.read().split(',')

                    accountnum = fields[0]
                    firstname = fields[1]
                    surname = fields[2]
                    email_addy = fields[3]
                    phonenum = fields[4]
                    accpassword = fields[5]
                    amount = fields[6]

                    while True:
                        legit_password = input('\nEnter your Account password: ')
                        if legit_password == accpassword:
                            print('You have logged in successfully')
                            break
                        else:
                            print('password not found')
            except FileNotFoundError:
                print( "User not found" )
        else:
            return False
            legit_user(legit_account, legit_password)



#operations

def transfer(amount):
    print('\n\n')
    print("=== TRANSFER FUNDS === \n\n")

    account = input('Enter the account number for the transfer:   ')
    try:
        valid_accnum()
        return account
    except:
        print("\nAccount number is invalid.")
                    
    transfer = int(input("\n How much do you want to transfer?:  "))
        
    # assumption1: mimimum and maximum withdrawal limits are ₦1000 and ₦50000 respectively

    if transfer < amount:
        try:
            if (transfer >= 50000):
                print( 'Maximum withdrawal limit exceeded. Please try again. ', end='\n\n' )
            elif (transfer <= 1000):
                print( 'Minimum withdrawal limit is 1000. Please try again. ', end='\n\n' )
            else:
                return transfer
                
        except:
            print("\n Account balance exceeded")
    else:
        print("\n Account balance exceeded")
                                
        amount -= transfer
        print("Transfer successful")

        #data.append([accnum, accountbal]):
        new_transaction()    

def new_transaction():

    while(True):
        new = int(input('\n\nDo you want to perform another transaction? \n            Yes [1] : No [2]   '))
        if (new == 1):
            bankops()
        elif (new == 2):
            logout()  
        else:
            print("Invalid option selected")
        break

def withdrawal(amount):
    print( '\n\n' )
    print( "=== WITHDRAW FUNDS === \n\n" )

    while (True):
        debit = int( input( 'How much would you like to withdraw?  \n' ) )

        # assumption1: mimimum and maximum withdrawal limits are ₦1000 and ₦50000 respectively

        if debit < amount:
            try:
                if (debit >= 50000):
                    print( 'Maximum withdrawal limit exceeded. Please try again. ', end='\n\n' )
                elif (debit <= 1000):
                    print( 'Minimum withdrawal limit is 1000. Please try again. ', end='\n\n' )
                else:
                    return debit
    
            except:
                print("\n Account balance exceeded")
        else:
            print("\n Account balance exceeded")
                                    
        amount -= debit
        print("Withdrawal successful")

        #data.append([accnum, accountbal]):
        new_transaction()    

def account_bal():
    print("\n========== CHECK BALANCE ========== \n\n")

    print (amount)

def complaints():

    print("\n====== LOG YOUR COMPLAINTS ====== \n")
    complaint = input('\nWhat issue will you like to report?  \n\n')
                
    print ('\n\nThank you for contacting us. We aim to respond to all complaints within 24 hours', end='\n\n')

    new_transaction()   

def deposit(amount):
    print("\n========== DEPOSITS ========== \n\n")
        
    depositamt = int(input('How much would you like to deposit?  '))
        
    amount += depositamt
    print ("Deposit successful\n")
    new_transaction()

def bankops():
    dt = datetime.datetime.now()
    dt_string = dt.strftime("Date: %d/%m/%Y Time: %H:%M")
    
    print ("\nACCOUNT ACCESSED AT #" + dt_string, end='\n\n')
            
    print ('These are the available options:', end='\n\n')
    print ('1. Withdrawal')
    print ('2. Cash Deposit')
    print ('3. Transfer')
    print ('4. Check balance')
    print ('5. Complaints')
    print ('6. Nothing else', end='\n\n')

    selectedOption = int(input('Please select an option:  '))
    if (selectedOption == 1):
        withdrawal()
    elif (selectedOption == 2):
        deposit()
    elif (selectedOption == 3):
        transfer()
    elif(selectedOption == 4):
        account_bal()
    elif(selectedOption == 5):
        complaints() 
    elif(selectedOption == 6):
        logout()     
    else:
        print('Invalid option selected! Please try again', end='\n\n')

def logout():

    dt = datetime.datetime.now()
    dt_string = dt.strftime("Date: %d/%m/%Y Time: %H:%M")
    print('\n====== THANK YOU FOR BANKING WITH US ====== \n')
    print('\n    YOU HAVE LOGGED OUT OF YOUR ACCOUNT \n')
    print ("       " + dt_string, end='\n\n')

def login():
    print("\n========== LOG INTO YOUR ACCOUNT ========== \n")
        
    legit_user(legit_account, legit_password)
    bankops()

def init():
    print("\n======= WELCOME TO LLOYDS TSB ======= \n\n")
    while (True):
        haveaccount = int(input("Do you have an account with us?: \n    YES [1] : NO [2]   "))
        if (haveaccount == 1):
            login()
        elif (haveaccount == 2):
            create_account()
        else:
            print("invalid option selected, try again \n")
  
    
    

    
#legit_user(legit_password, legit_password)
#find_account(accountnum)
#read_account_rec(4503488858)
#create_account()
#find_password(4503488858)
#registered_user()
#'cdfXS34$'
