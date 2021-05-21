sum = 0
num = int(input("Enter number for checking number is perfect or not = "))
for i in range(1,num//2+1):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print("Number is perfect Number")
else:
    print("Number is not perfect Number")