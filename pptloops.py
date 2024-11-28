# Name: Isabell Davis
# Prog Purpose: This program finds the Personal Property Tax on vehicles
#   Personal Property Tax rate: 4.40% per year
#   Tax Relief: 30%

import datetime

##############  define global variables ################
# define, personal property tax rate, and tax relief
PPT_RATE = .0440
TAX_RELIEF = .30

# define global variables
veh_val = 0
ppt_rate = 0
tax_relief = 0
full_tamount = 0
total = 0

###############  define program functions ##############
def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tax for another vehicle (Y or N)?")
        if yesno == "N" or yesno =="n":
            more = False
            print("Personal Property tax due JUNE 05")

def get_user_data():
    global veh_val, inout
    print('********* Personal Property Tax *******')
    veh_val = int(input('Assesed value of the vehicle: '))
    inout = int(input('Is your vehicle eligible for tax relief? (1 for YES, 2 for NO)'))

def perform_calculations():
    global ppt_rate, tax_relief, full_tamount, total

    if inout == 1:
        ppt_rate = veh_val * PPT_RATE 
        tax_relief = ppt_rate * TAX_RELIEF
        full_tamount = ppt_rate - tax_relief
        total = full_tamount / 2

    else:
        ppt_rate = veh_val * PPT_RATE
        tax_relief = 0
        full_tamount = ppt_rate
        total = full_tamount / 2

def display_results():
    currency = '8,.2f'
    line = '--------------------------------'
    
    print(line)
    print('***** Personal Property Tax *******')
    print('   Please Pay in a Timely Manner   ')   
    print(str(datetime.datetime.now()))
    print(line)
    print('Assesed Value     $ ' + format(veh_val,currency))
    print('Tax Relief        $ ' + format(tax_relief,currency))
    print('Full Total Amount $ ' + format(full_tamount,currency))
    print(line)
    print('Total Due         $ ' + format(total, currency))


########    calls on main program to execut #########
main()
        
    

