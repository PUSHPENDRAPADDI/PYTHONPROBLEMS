dupnum=0
temp=0
sum=0
sqa=1
num =int(input("Enter number to ckeck whether number is happy or not = "))
if num>9:
    dupnum=num
while dupnum > 9:
    while dupnum!=0:
        temp = dupnum%10
        print(temp," temp hai")
        sqa = temp*temp
        dupnum = dupnum//10
        print(dupnum," hai")
    sum = sum + sqa
    dupnum=sum
    sum=0
if dupnum==1:
    print(num," is happy number")
else:
    print(num," is not happy number")