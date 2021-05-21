ch = input("Enter your string to check symetric =")
mid=0
flag=0
n = len(ch)
if n%2:
    mid = n//2+1
else:
    mid = n//2
start1 = 0
start2 = mid
while(start1 <mid and start2 <n):
    if (ch[start1] == ch[start2]):
        start1 = start1 + 1
        start2 = start2 + 1
    else:
        print("Number is not symetric")
        flag=1
        break
if (flag == 0):
    print("String is symetric") 
else:
    print("String is not symetric")