arr1 = [1,2,3,4,5,6,7,8,9]
arr2 = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(arr1)):
    for j in range(0,i+1):
        arr2[i] = arr2[i]+arr1[j]
    print(arr2[i],end = " ")