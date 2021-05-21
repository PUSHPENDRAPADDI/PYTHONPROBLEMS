name = input("Enter your name :- ")
unit = int(input("Enter your unit :- "))
if unit >0 and unit <= 50:
    charge = 0.50*unit
elif unit >50 and unit <=150:
    charge = 25+ ((unit - 50)*0.75)    
elif unit >150 and unit <= 250:
    charge = 100 + ((unit-150)*1.20)
elif unit > 250:
    charge = 220 + ((unit-250)*1.50)     
surcharge = (20*charge)/100
bill = surcharge + charge
print(name," electric bill is :- ", bill)       