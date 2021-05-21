arr = [1,2,3,4,5,6,7,8,9]
num = len(arr)
temp = arr[0]
arr[0] = arr[num-1]
arr[num-1] = temp
for i in range(num):
    print(arr[i])    