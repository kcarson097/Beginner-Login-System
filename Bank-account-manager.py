#Bank Account Manager - Create a class called Account which will be an abstract class for three other classes called CheckingAccount, 
#SavingsAccount and BusinessAccount. 
#Manage credits and debits from these accounts through an ATM style program.

#withdraw
#deposit



#Project Scope
#To tackle this project, first consider what has to happen.
#There will be three different types of bank account (Checking, Savings, Business)
#Each account will accept deposits and withdrawals, and will need to report balances

#create a general account class with basic functionality
class Account():
    
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        print('Please see your account details below :')
        print('Account Owner : {}'.format(self.owner))
        print('Account Balance: {}'.format(self.balance))
        
    
    def withdraw(self,wd):
        self.wd = wd
        #self.balance -= self.wd
        if self.wd > self.balance:
            print('Sorry you do not have enough funds')
        else:
            self.balance -= self.wd
            print('Transanction successful')
            print('Your new balance is £{}'.format(self.balance))
            
    def deposit(self,dp):
        self.dp = dp
        self.balance += self.dp
        print('Transaction sucessful')
        print('Your new balance is £{}'.format(self.balance))

#checking account class
class Checking_account(Account):
    
    def __init__(self,owner, balance):
        # super() calls init method from account class (saves rewriting it)
        super().__init__(owner,balance)
        
    def __str__(self):
        return 'Checking account balance : {} '.format(self.balance)


class Savings_account(Account):
    
    def __init__(self,owner,balance):
        super().__init__(owner,balance)
    
    def __str__(self):
        return 'Savings account balance : {}'.format(self.balance)


class Business_account(Account):
    
    def __init__(self,owner,balance):
        super().__init__(owner,balance)
    
    def __str__(self):
        return 'Business account balance : {}'.format(self.balance)


#class to store customer details
class Customer()    
    def __init__(self,name,PIN):
        self.name = name
        self.PIN = PIN
        self.accts = {'C':[], 'S':[], 'B':[]}
        
    def open_checking_account(self,acct_nbr,int_dp):
        self.acct_nbr = acct_nbr
        self.int_dp = int_dp
        
        self.accts['C'].append(Checking_account(acct_nbr,int_dp))
    
    def open_savings_account(self,acct_nbr,int_dp):
        self.acct_nbr = acct_nbr
        self.int_dp = int_dp
        
        self.accts['S'].append(Savings_account(acct_nbr,int_dp))
        
        
        
    def open_business_account(self,acct_nbr,int_dp):
        self.acct_nbr = acct_nbr
        self.int_dp = int_dp
        
        self.accts['B'].append(Business_account(acct_nbr,int_dp))
        
class Checking_account(Account):
    
    def __init__(self,owner, balance):zz
        
    def __str__(self):
        return 'Checking account balance : {} '.format(self.balance)
    