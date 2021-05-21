# num=1401601499
num = int(input("Enter the number for ISBN = "))
dupnum=num
temp=0
sum=0
mul=1
for i in range(10,-1,-1):
    temp=dupnum%10
    mul=temp*i
    sum=sum+mul
    dupnum=dupnum/10
if sum%11==0:
    print("The ISBN is correct")
else:
    print("The is not correct")