import pickle
import os
class Account:
    def __init__(self):
        self.__name = input("Enter Your Name: ")
        self.__password = input("Enter your password: ")
        while True:
            self.__balance = int(input("Enter starting balance (min 5000): "))
            if self.__balance >= 5000:
                break

    @staticmethod
    def login():
        print("-------")
        Account.admin()
        print("-------")
        id,password = input("Enter id and password: ").split()
        file=open("accounts.bin",'rb')
        file1 = open("temp.bin",'wb')
        obj = None
        while True:
            try:
                person = pickle.load(file)
                if (id==person.__name and password==person.__password):
                    obj = person
                else:
                    pickle.dump(person,file1)
            except:
                break
        file.close()
        file1.close()
        os.remove('accounts.bin')
        os.rename('temp.bin','accounts.bin')
        return obj

    @staticmethod
    def admin():
        file = open('accounts.bin','rb')
        while True:
            try:
                s = pickle.load(file)
                print(s.__name)
            except:
                break
        file.close()
    
    def logout(self):
        file=open("accounts.bin",'wb')
        pickle.dump(self, file)
        file.close()


    def deposit(self):
        while True:
            money = int(input("Enter Amount to be deposited (min: 500): "))
            if money>=500:
                break
        self.__balance+=money

    def withdraw(self):
        money = int(input("Enter Amount to withdraw: "))
        self.__balance-=money

    def bal(self):
        print(self.__balance)

prompt = '''Enter Your Choice:
1. Create Account
2. Login
'''
user = None
while True:
    if user==None:
        print(prompt)
        user = Account() if int(input())==1 else Account.login()
        print(user)
        print(type(user))
    else:
        print(user)
        print(type(user))
        print("Enter your choice","1. Check Your details","2. Deposit","3. Withdraw","4. Log out",sep='\n')
        c = int(input())
        if c==1:
            user.bal()
        elif c==2:
            user.deposit()
        elif c==3:
            user.withdraw()
        elif c==4:
            user.logout()
            user = None
            Account.admin()
        else:
            pass