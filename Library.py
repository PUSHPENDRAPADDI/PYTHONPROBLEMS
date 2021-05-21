name = input("Enter your name :- ")
day = int(input("Enter number of days :- "))
if day >0 and day <=5:
    charge = 40*day
elif day>5 and day<=10:
    charge = 65*day   
elif day>10:
    charge = 80*day    
print(name," Fine for ",day," days late is :- ", charge, "paisa")    