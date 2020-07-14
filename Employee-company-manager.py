class Employee():
    
    def __init__(self,f_name, l_name,contract):
        
        self.f_name = f_name
        self.l_name = l_name
        self.contract = contract

class Hourly_employee(Employee):
    
    def __init__(self,f_name, l_name,contract):
        
        self.f_name = f_name
        self.l_name = l_name
        self.contract = contract
        self.bank = 0
        
    def pay_employee(self,hourly_rate):
        
        self.hourly_rate = hourly_rate
        self.hours_worked = int(input('Please ENTER the amount of hours worked'))
        self.pay = self.hours_worked * self.hourly_rate 
        self.bank += self.pay
        
        print('Payment succesful')
        print('Employees bank : ' + str(self.bank))
        
    def __str__(self):
        return 'Name' + ' : ' + self.f_name + ' ' + self.l_name

class Salary_employee(Employee):
    
    def __init__(self,f_name, l_name,contract):
        
        self.f_name = f_name
        self.l_name = l_name
        self.contract = contract
        self.bank = 0
        
    def pay_employee(self,salary):
        
        self.salary = salary 
        self.bank += self.salary
        print('Payment Successful')
        print('Employees bank : ' + str(self.bank))
        
    def __str__(self):
        return 'Name' + ' : ' + self.f_name + ' ' + self.l_name
        
class Manager_employee(Employee):

    
    def __init__(self,f_name, l_name,contract):
        
        self.f_name = f_name
        self.l_name = l_name
        self.contract = contract
        self.bank = 0
        
    def pay_employee(self,salary):
        
        self.salary = salary 
        self.bank += self.salary
        print('Payment Successful')
        print('Employees bank : ' + str(self.bank))
        
    def __str__(self):
        return 'Name' + ' : ' + self.f_name + ' ' + self.l_name

class Company():
    
    #hire, raise and fire employees
    #keep track of all employees
    
    def __init__(self):
        
        self.database = {'H' :[] , 'S' : [] , 'M' : []}
        
    def add_hourly(self):
        
        f_name = input('ENTER first name')
        l_name = input('ENTER last name')
        contract = 'hourly'
        self.database['H'].append(Hourly_employee(f_name , l_name, contract).__str__())
        
    
    def add_salary(self):
        
        f_name = input('ENTER first name')
        l_name = input('ENTER last name')
        contract = 'salary'
        self.database['S'].append(Salary_employee(f_name,l_name,contract).__str__())
        
    def add_manager(self):
        
        f_name = input('ENTER first name')
        l_name = input('ENTER last name')
        contract = 'manager' 
        self.database['M'].append(Manager_employee(f_name,l_name,contract).__str__())
        
    
    def fire(self,f_name , l_name , contract):
        if contract.lower() == 'hourly':
            print('Employee {} {} is fired'.format(f_name,l_name))
            self.database['H'].remove(Hourly_employee(f_name,l_name,contract).__str__())
        if contract.lower() == 'salary':
            print('Employee {} {} is fired'.format(f_name,l_name))
            self.database['S'].remove(Salary_employee(f_name,l_name,contract).__str__())
        if contract.lower() == 'manager':
            print('Employee {} {} is fired'.format(f_name,l_name))
            self.database['S'].remove(Salary_employee(f_name,l_name,contract).__str__()) 


    def raised(self,f_name, l_name, contract,raised):
        if contract[0].lower() == 'h':
                self.database['H'].remove(Hourly_employee(f_name,l_name,contract).__str__())
                if raised.lower() == 'salary' :
                    self.database['S'].append(Salary_employee(f_name,l_name,contract).__str__())
                    print('Employee {} {} is raised'.format(f_name,l_name))
                else:
                    self.database['M'].append(Manager_employee(f_name,l_name,contract).__str__())
                    print('Employee {} {} is raised'.format(f_name, l_name))
                    
        elif contract[0].lower() == 's':
                self.database['H'].remove(Salary_employee(f_name,l_name,contract).__str__())
                if raised.lower() == 'manager':
                    self.database['M'].append(Manager_employee(f_name,l_name,contract).__str__())
                    print('Employee {} {} is raised'.format(f_name, l_name))
                
         
                
        def view_database(self):
            for employee in self.database.items():
                print(employee)