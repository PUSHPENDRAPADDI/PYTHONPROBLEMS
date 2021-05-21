num = int(input("Enter the number to print the pattern = "))
for i in range(0,num):
    for j in range(0, num):
        if j >= num-i:
            print(i,end=' ')
        else:
            print(" ",end=' ') 
    print('') 
for i in range(0,num):
    for j in range(0, num):
        if j >= i:
            print(i,end=' ')
        else:
            print(" ",end=' ') 
    print('') 