num = int(input("Enter number for checking prime or not = "))
count = 0
for i in range(2, num):
    if num%i == 0:
        count = count + 1
if count>=1:
    print(num," is not prime")
else:           
    print(num," is prime")        