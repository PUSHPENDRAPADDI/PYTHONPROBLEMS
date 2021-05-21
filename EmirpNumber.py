num = int(input("Enter number for checking EmirpNumber = "))
num2= 0
numO = num
while numO!=0:
    temp = numO%10
    num2 = num2*10+temp
    numO = numO//10
count = 0
for i in range(2, num):
    if num%i == 0 and num2%i==0:
        count = count + 1
if count>=1:
    print(num," is not EmirpNumber")
else:           
    print(num," is EmirpNumber")   