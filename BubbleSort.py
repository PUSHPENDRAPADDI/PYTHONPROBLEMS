num = [5,4,3,2,1,9,8,7,6]
temp = 0
for i in range(len(num)): 
    for j in range(len(num)):
        if num[i] > num[j]:
            temp = num[j]
            num[j] = num[i]
            num[i]=temp
for i in range(len(num)):
    print(num[i],end =" ")
        