num = int(input("Enter number = "))
num2 = bool(input("Enter any key or just hit enter = "))
if num2 == True:
    for i in range(0,num+1):
        for j in range(0, i):
            print("*",end=' ')
        print()
else:
    for i in range(0,num+1):
        for j in range(0, num-i):
            print("*",end=' ')
        print()