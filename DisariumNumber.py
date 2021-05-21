num = int(input("Enter number To check whether number is disarium or not = "))
numo = num
num2 = num
sum = 0
sqa = 0
count=0
temp =0
while num != 0:
    num = num//10
    count=count+1
while count !=0:
    temp = numo%10
    sqa = pow(temp,count)
    sum = sum+sqa
    count = count-1
    numo = numo//10
if num2 == sum:
    print(num2," is disarium Number")
else:
    print(num2," is not disarium Number")