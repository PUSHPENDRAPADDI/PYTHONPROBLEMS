num = int(input("Enter number for Automoefic number = "))
count=0
numo=num
sum=0
sum2=0
ponum = pow(num,2)
ponum2 = 0
while num!=0:
    num=num//10
    count-=1
while count!=0:
    ponum2 = ponum%10
    sum = sum*10+ponum2
    ponum=ponum//10
    count+=1
ponum2=0
while sum!=0:
    sum2 = (sum2*10) + sum%10
    sum=sum//10
if sum2==numo:
    print("The number is Automorfic")
else:
    print("The number is not Automorfic")