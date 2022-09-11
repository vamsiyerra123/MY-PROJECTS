customers_dictionary={112233445566771:{'Name':'Ramu','Address':'SR Nagar, Hyd','Mobile Number':9988776655,'Email ID':'ramu@gmail.com','IFSC Code':'SBIN00011','PIN':1122,'Account Type':'Savings','Account Balance':10000},
                      112233445566772:{'Name':'Raju','Address':'Ameerpet, Hyd','Mobile Number':9988776651,'Email ID':'raju@gmail.com','IFSC Code':'SBIN00011','PIN':2233,'Account Type':'Savings','Account Balance':20000},
                      112233445566772:{'Name':'Roja','Address':'Kukatpally, Hyd','Mobile Number':9988776652,'Email ID':'roja@gmail.com','IFSC Code':'SBIN00011','PIN':3344,'Account Type':'Savings','Account Balance':30000},
                      112233445566773:{'Name':'Ramesh','Address':'Bachupalli, Hyd','Mobile Number':9988776653,'Email ID':'ramesh@gmail.com','IFSC Code':'SBIN00011','PIN':4455,'Account Type':'Savings','Account Balance':40000}}
print("Welcome to the Bank")
print("****************************")
account_number=int(input("Dear customer, please enter your 15-digit account number:"))
if account_number not in customers_dictionary:
    print("Your account number does not exist. Bye")
    exit()

PIN=int(input("Dear customer, please enter your PIN number:"))
for i in customers_dictionary:
    if customers_dictionary[account_number]['PIN']!=PIN:
        print("Dear customer, your PIN is invalid. Bye")
        exit()

ans="yes"
while ans=="yes":
    print("*************")
    print("Operations")
    print("*************")
    print("1. Display Account Details")
    print("2. Balance Display")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Change PIN Number")
    choice=int(input("Dear customer, please enter your choice:"))
    if choice==1:
        print("Customer Name:",customers_dictionary[account_number]['Name'])
        print("Account Number:",account_number)
        print("Account Type:",customers_dictionary[account_number]['Account Type'])
        print("Account Balance:",customers_dictionary[account_number]['Account Balance'])
        print("IFSC Code:",customers_dictionary[account_number]['IFSC Code'])
        print("Customer Address:",customers_dictionary[account_number]['Address'])
        print("Customer Mobile Number:",customers_dictionary[account_number]['Mobile Number'])
        print("Customer Email id:",customers_dictionary[account_number]['Email ID'])
    elif choice==2:
        print("Account Balance:",customers_dictionary[account_number]['Account Balance'])
    elif choice==3:
        print("Your Account Balance:",customers_dictionary[account_number]['Account Balance'])
        deposit_amount=int(input("Dear customer, please enter deposit amount:"))
        customers_dictionary[account_number]['Account Balance']+=deposit_amount
        print("After depositing,",deposit_amount," total account balance=",customers_dictionary[account_number]['Account Balance'])
    elif choice==4:
        print("Your Account Balance:",customers_dictionary[account_number]['Account Balance'])
        withdraw_amount=int(input("Dear customer, Please enter withdraw amount:"))
        if withdraw_amount<=customers_dictionary[account_number]['Account Balance']:
            customers_dictionary[account_number]['Account Balance']-=withdraw_amount
            print("After withdrawing",withdraw_amount," total account balance=",customers_dictionary[account_number]['Account Balance'])
        else:
            print("Insufficient Funds")
    elif choice==5:
        old_pin=int(input("Dear customer, please enter old PIN number:"))
        if customers_dictionary[account_number]['PIN']==old_pin:
            new_pin=int(input("Dear customer, please enter your New PIN number:"))
            customers_dictionary[account_number]['PIN']=new_pin
            print(old_pin,"is changed to",new_pin)
        else:
            print("Invalid PIN number")
    else:
        print("Invalid choice")
    ans=input("Do you want to continue(yes/no):")
