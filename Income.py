income = float(input("Enter income of employee in lakh= "))
tax =0
if income <=2.5:
    tax = 0
elif income>2.5 and income <= 5:
    tax = (income-2.5)*0.05
elif income>5 and income <= 10:
    tax = 0.125 + (income-5)*0.2
elif income>10:
    tax = 1.25 + (income-10)*0.3
print("Total tax paid by the employee is ",tax,"lakh")    