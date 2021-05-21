num = int(input("Enter your number for checking Armstrong = "))
num3 = num2 = num
temp = temp1 = count = arm = result = 0
while num!=0:
    temp = num%10
    num = num//10
    count = count+1
while num2 != 0:
    temp1 = num2%10  
    num2 = num2//10
    result = pow(temp1 , count)
    arm = arm+result
if arm == num3:
    print(num3," is Armstrong number")     
else:
    print(num3," is not a Armstrong number")     