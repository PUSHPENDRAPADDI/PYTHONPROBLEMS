num = int(input("Enter the number to print the pattern = "))
ch = 'A'
for i in range(0,num):
    ch2 = ch
    for j in range(0, num-i):
        print(ch2,end=' ')
        ch2 = chr(ord(ch2)+1)
    print('') 