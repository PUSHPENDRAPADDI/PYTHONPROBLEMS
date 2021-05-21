rentalCharge = 130
name = input("Enter your name :- ")
call = int(input("Enter number of calls :- "))
if call >0 and call <=100:
    charge = rentalCharge
elif call>100 and call<=200:
    charge = rentalCharge + (call*1)
elif call>200 and call<=300:
    charge = rentalCharge+(call*0.50)    
elif call>300 and call<=500:
    charge = rentalCharge+(call*0.20)    
elif call>500:
    charge = rentalCharge+(call*0.10)    
print(name," Telephone bill is :- ", charge)    