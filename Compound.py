pri = int(input("Enter principle = "))
time = int(input("Enter time = "))
rate = float(input("Enter rate = "))
a = pri * (pow((1+rate/100) , time))
ci = a - pri
print("Compound interest is = ", ci)