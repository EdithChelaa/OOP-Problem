# wallet.py
from user import Base, engine
from sqlalchemy import create_engine
from user import User, Transaction
from sqlalchemy.orm import sessionmaker
import re

#initialize
Base.metadata.create_all(engine)

engine = create_engine('sqlite:///users.db')  
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#function to create User

def create_user(username, password):
    if not isinstance(username, str) or not username:
        print("Username must be a non-empty string.")
        return
    elif not re.match("^[a-zA-Z]+$", username):
        print("Username must contain only letters!!!")
        return
    
    existing_user = session.query(User).filter(User.username == username).first()
    
    if existing_user:
        print("Username already exists!!!")
    else:
        if not password:
            print("Password must be a non-empty string.")
            return
        
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        print(f"User {username} added successfully.")

#function for authentication
def authenticate(username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    return user

#function to deposit funds
def deposit(username,password, amount):
    user = authenticate(username,password)
    if user:
        if amount > 0:
            user.balance += amount
            transaction = Transaction(user=user, type='deposit', amount=amount)
            session.add(transaction)
            session.commit()
            print(f"Deposited {amount} into {username}'s wallet. New wallet balance: {user.balance} coins")
        else:
            print("Amount to Deposit must be more than 0 coins!!!")
    else:
        print(f"User {username} not found or invalid password.")
        

#function for widthrawing
def withdraw(username, password, amount):
    user = authenticate(username, password)
    if user:
        if amount > 0:
            if user.balance >= amount:
                user.balance -= amount
                session.commit()
                print(f"Withdrew {amount} coins from {username}'s wallet. New wallet balance: {user.balance}")
            else:
                print("Sorry, Insufficient coins in your wallet.")
        else:
            print("Amount to withdraw must be more than 0 coins!!!")
    else:
        print(f"invalid passord or user {username} not found.")
        

#function for transfering
def transfer(sender, recipient, password, amount):
    sender_user = authenticate(sender, password)
    recipient_user = session.query(User).filter_by(username=recipient).first()

    if sender_user and recipient_user:
        if amount > 0:
            if sender_user.balance >= amount:
                withdraw(sender, password, amount)
                deposit(recipient, password, amount)
                print(f"Transferred {amount} coins from {sender} to {recipient}'s wallet")
            else:
                print("Insufficient funds.")
        else:
            print("Amount to transfer must be greater than 0 coins!!!")
    else:
        print(f"User not found. Check sender: {sender} and recipient: {recipient} or invalid password")


#function for checking balance
def get_balance(username,password):
    user = authenticate(username,password)
    if user:
        print(f"{username}'s current coins: {user.balance}")
    else:
        print(f"User {username} not found. or invalid password")


# functoion to delete the user by username
def delete_user_by_name(username, password):
    user = authenticate(username, password)
    if user:
        session.query(Transaction).filter(Transaction.user_id == user.id).delete()
        
        session.delete(user)
        session.commit()
        print(f"User {username} deleted successfully.")
    else:
        print("Invalid username or password.")

# function to delete the user by id
def delete_user_by_id(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.query(Transaction).filter(Transaction.user_id == user.id).delete()
        
        session.delete(user)
        session.commit()
        print(f"User with ID {user_id} deleted successfully.")
    else:
        print(f"User with ID {user_id} not found.")




