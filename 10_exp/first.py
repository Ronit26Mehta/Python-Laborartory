import mysql.connector

# Open database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ronit",
    database="testdb"
)

# Create a cursor object
cursor = db.cursor()

# Create a table for the banking system if it doesn't exist
create_table_sql = '''
    CREATE TABLE IF NOT EXISTS accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        account_number INT NOT NULL,
        initial_balance INT,
        rate_of_interest INT,
        contact_number VARCHAR(255),
        address_field VARCHAR(255)
    )
'''
cursor.execute(create_table_sql)

def create_account(n):
    for i in range(n):
        username = input("Enter the name of the user: ")
        balance = int(input("Enter the balance of the user: "))
        account = int(input("Enter the account number of the user: "))
        rate_of_interest = int(input("Enter the rate of interest: "))
        contact_number = input("Enter the contact number: ")
        address_field = input("Enter address field: ")

        # Prepare SQL query to INSERT a record into the database
        insert_sql = '''
            INSERT INTO accounts(username, account_number, initial_balance, rate_of_interest, contact_number, address_field)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (username, account, balance, rate_of_interest, contact_number, address_field)
        try:
            # Execute the SQL command
            cursor.execute(insert_sql, values)
            # Commit your changes in the database
            db.commit()
            print("Details inserted.")
        except Exception as e:
            print("Error:", e)
            # Rollback in case there is any error
            db.rollback()

def deposit():
    username = input("Enter your username: ")
    amount = int(input("Enter the amount to deposit: "))

    # Update the balance
    update_sql = '''
        UPDATE accounts
        SET initial_balance = initial_balance + %s
        WHERE username = %s
    '''
    values = (amount, username)
    try:
        cursor.execute(update_sql, values)
        db.commit()
        print("Deposit successful.")
    except Exception as e:
        print("Error:", e)
        db.rollback()

def withdraw():
    username = input("Enter your username: ")
    amount = int(input("Enter the amount to withdraw: "))

    # Update the balance
    update_sql = '''
        UPDATE accounts
        SET initial_balance = initial_balance - %s
        WHERE username = %s
    '''
    values = (amount, username)
    try:
        cursor.execute(update_sql, values)
        db.commit()
        print("Withdrawal successful.")
    except Exception as e:
        print("Error:", e)
        db.rollback()

def compute_interest():
    username = input("Enter your username: ")
    
    # Calculate interest and display
    select_sql = '''
        SELECT initial_balance, rate_of_interest
        FROM accounts
        WHERE username = %s
    '''
    values = (username,)
    try:
        cursor.execute(select_sql, values)
        result = cursor.fetchone()
        if result:
            initial_balance, rate_of_interest = result
            interest = (initial_balance * rate_of_interest) / 100
            print("Interest: ", interest)
        else:
            print("User not found.")
    except Exception as e:
        print("Error:", e)

def dispbalance():
    username = input("Enter your username: ")

    # Display balance
    select_sql = '''
        SELECT initial_balance
        FROM accounts
        WHERE username = %s
    '''
    values = (username,)
    try:
        cursor.execute(select_sql, values)
        result = cursor.fetchone()
        if result:
            balance = result[0]
            print("Balance: ", balance)
        else:
            print("User not found.")
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Compute Interest\n5. Display Balance\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            num = int(input("Enter the number of accounts to create: "))
            create_account(num)
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            compute_interest()
        elif choice == '5':
            dispbalance()
        elif choice == '6':
            break
        else:
            print("Enter a valid choice.")

# Run the main function to start the application
if __name__ == "__main__":
    main()

# Close the database connection when done
db.close()
