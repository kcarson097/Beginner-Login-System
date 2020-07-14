#Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.

# function that calculates tax and returns total 

def calc_tax(cost,tax):
    #convert tax input into a percentage
    tax_percent = tax/100
    #multiply tax_percentage by given cost to calculate tax 
    total_cost = 0
    taxed_amount = tax_percent * cost
    #calculate total cost with tax
    total_cost = cost + taxed_amount 
   
    
    print('Thank you ! See below your calculated tax. Have a nice day :)')
    print('\n')
    print('Amount of tax (%) : {}'.format(taxed_amount))
    print('Total cost (£) with VAT:{}'.format(total_cost))


def ask_tax():
    while True:
        try:
            tax = int(input('Please enter the state tax (%)'))
        except:
            tax = int(input('Whoops you must enter an integer value ! Try again'))    
        finally:
                return tax

def ask_cost():
    while True:
        try:
            cost = int(input('Please enter the cost of your purchase (£) '))
        except:
            cost = int(input('Whoops you must enter an integer value ! Try again'))
        finally:
            return cost

working = True

while working:

    print('Hello,thank you for using our service')
    print('\n')

    tax = ask_tax()
    print('\n')

    cost = ask_cost()
    print('\n')

    calc_tax(cost,tax)
    print('\n')
    
    new_calc = input('Would you like to make a new calculation ? ENTER y or n')
    
    if new_calc[0].lower() == 'y':
        continue
    elif new_calc[0].lower() == 'n':
            working = False
            break
    else:
         print('Sorry please try again. ENTER y or n')
         new_calc = input('Enter y or n')

