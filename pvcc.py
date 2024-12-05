# Name: Isabell Davis
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https:/www.pvcc.edu/tuition-and-fees
#   Price for Tuition In: $164.40
#   Price for Tuition Out: $353.00
#   Capital fee: $26.00    
#   Institution fee: $1.75
#   Activity fee: $2.90

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 164.40
RATE_TUITION_OUT = 353.00
RATE_CAPITAL_FEE = 26.00
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

# create output file
outfile = 'pvccweb.html'

##############  define program functions ##############
def main():

    open_outfile()
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()
            print("Thank you for enrolling at PVCC. Enjoy the semester!")

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Piedmont Virginia Comm College Tuition & Fees </title>\n')
    f.write('<style> td{text-align: center} </style> </head>\n')
    f.write('<body style ="background-color: #e785b9; background-image: url(wp-pvcc.jpeg); color: #000000;">\n')
    
def get_user_data():
    global inout, numcredits, scholarship_amt
    print('**** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees ****')
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarship_amt = int(input("Scholarship amount received: "))

    
def perform_calculations():
    global tuition, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition = numcredits * RATE_TUITION_IN
        inst_fee = numcredits * RATE_INSTITUTION_FEE
        act_fee = numcredits * RATE_ACTIVITY_FEE
        total = tuition + inst_fee + act_fee
        balance = scholarship_amt - total
        cap_fee = 0
        
    else:
        tuition = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE
        inst_fee = numcredits * RATE_INSTITUTION_FEE
        act_fee = numcredits * RATE_ACTIVITY_FEE
        total = tuition + cap_fee + inst_fee + act_fee
        balance = scholarship_amt - total

#calculations for the other fees, total, and balance go here

def display_results():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]
    line = '----------------------------------------'

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan = "3">'
    sp = " "

    f.write('\n<table border="3" style="background-color: #e785b9; font-family: arial; margin: auto;">\n')
    f.write(colsp + '\n')
    f.write('<h2>PIEDMONT VIRGINIA COMM COLLEGE</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('**** Tuition and Fees Report****\n')
    
    f.write(tr + 'Tuition' + endtd + str(tuition) + endtd + format(tuition,currency) + endtr)
    f.write(tr + 'Institution Fee' + endtd + str(inst_fee) + endtd + format(inst_fee,currency) + endtr)
    f.write(tr + 'Activity Fee' + endtd + str(act_fee) + endtd + format(act_fee,currency) + endtr)
    f.write(tr + 'Capital Fee' + endtd + str(cap_fee) + endtd + format(cap_fee,currency) + endtr)
    
    f.write(tr + 'Total' + endtd + sp + endtd + format(total,currency) + endtr)
    f.write(tr + 'Scholarship' + endtd + sp + endtd + format(scholarship_amt,currency) + endtr)
    f.write(tr + 'Balance' + endtd + sp + endtd + format(balance,currency) + endtr)

    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')


##########  calls on main program to execut #########
main()
