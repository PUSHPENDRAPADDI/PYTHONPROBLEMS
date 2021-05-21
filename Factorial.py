num = int(input("Enter number for factorial = "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print("the factorial of ",num," is ",fact)    