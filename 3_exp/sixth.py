account_catalog = {"username":[],"account_number":[],"intial-balance":[],"rate-of-interset":[],"contact-number":[],"address-field":[]}
def create_account(n):
     username = str(input("Enter the name of user"))
     balance = int(input("Enter the balance of user"))
     account = int(input("enter the account number of user"))
     rate_of_interset= int(input("Enter the rate of the interest"))
     contact_number = int(input("enter the contact number"))
     address_field = str(input("Enter address field"))
     for i in range(n):    
       account_catalog["username"].append(username)
       account_catalog["account_number"].append(account)
       account_catalog["intial-balance"].append(balance)
       account_catalog["rate-of-interset"].append(rate_of_interset)
       account_catalog["contact-number"].append(contact_number)
       account_catalog["address-field"].append(address_field)
     print("details inserted")
 
def deposit():
    print("Enter your username")
    name = input()
    data = account_catalog["username"].index(name)
    n = int(input("Enter the amount:"))
    account_catalog["intial-balance"][data] =  account_catalog["intial-balance"][data] + n
    print("value updated")
def withdraw():
    print("Enter your username")
    name = input()
    data = account_catalog["username"].index(name)
    n = int(input("Enter the amount:"))
    account_catalog["intial-balance"][data] =  account_catalog["intial-balance"][data] - n
    print("value updated")
def compute_interest():
    print("Enter your username")
    name = input()
    data = account_catalog["username"].index(name)
    intrest =  account_catalog["intial-balance"][data] * account_catalog["rate-of-interset"][data]/100
    print("value:",intrest)
def dispbalance():
    print("Enter your username")
    name = input()
    data = account_catalog["username"].index(name)
    print("balance:",account_catalog["intial-balance"][data])
def main():
    value = True
    while value !=False:
        print("\n1.create Account \n2.Deposit \n3.withdraw \n4.compute_interest \n5.dispblance \n6.exit")
        n = int(input("Enter your choice"))
        if n ==1:
            num = int(input("enter the accounts to be created"))
            create_account(num)
        elif n == 2:
            deposit()
        elif n == 3:
            withdraw()
        elif n == 4:
            compute_interest()
        elif  n == 5:
            dispbalance()
        elif n == 6:
            value = False
        else:
            print("Enter valid choice")
main()
            
    


