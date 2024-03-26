import math
while True:

    menu = '''
    Hello! We are here to help you with your finance. 

    investment - to calculate the amount of interest you'll earn on your investment
    bond       - to calculate the amount you'll have to pay on a home loan

    '''

    print(menu)
    select = input ("Enter either 'investment' or 'bond' from the menu above to proceed or type 'quit' to exit : ").lower()

    if select == "investment":
        #P is the amount that the user deposits 
        P = float(input ("Please enter the amount you like to deposit: ")) 
        #r is the rate of interest as a percent %
        r = float(input ("Please enter the rate of interest (exclude the % symbol): ")) /100
        #t is the amount of years of investment
        t = float(input ("Please enter the years for investment: ")) 

        calculation_select = input("Please enter either 'simple' or 'compound' interest: ").lower

        #cant get this work when picking simple or compound, gets straight to invalid selection. any help would be great
        if calculation_select == "simple" :

            print(P *(1 + r*t))
            continue

        elif calculation_select == "compound" :
        
            print(P * math.pow((1 + r), t))
            continue
    
        else:
            print("Invalid selection.")
            continue

    elif select == "bond":
    
        #P is the present value of the house
        P = float(input ("Please enter the present value of the house: ")) 
        #i is the monthly interest rate
        i = float(input ("Please enter the rate of interest (exclude the % symbol): ")) /100
        i = i / 12
        #n is the number of months over which the bond will be repaid
        n = float(input ("Please enter the months planned for repayment: ")) 

        print((i * P) / (1 - (1 + i)** (-n)))
        continue

    elif select == "quit":
        print("Exiting . . .")
        break
    
    else:
        print("Invalid selection.")
        continue 
