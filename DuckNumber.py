num = int(input("Enter number for checking whether number is duck or not = "))
count=0
temp = 0
while num != 0:
    temp = num % 10
    num = num // 10
    if temp == 0:
        count=count+1
if temp != 0 and count >0:
    print("It is duck number")
else:
    print("It is not duck number")