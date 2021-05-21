num = int(input("Enter the number for prime number = "))
count = 0
for i in range(1,num+1):
    for j in range(2,i):
        if i%j ==0:
            count = count +1
    if count == 0:
        print(i," is prime number")
    count = 0    