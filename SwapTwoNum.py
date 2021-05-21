arr = [1,2,3,4,5,6,7,8,9]
num = int(input("Enter first number to swap = "))
num2 = int(input("Enter second number to swap = "))
temp = arr[num-1]
arr[num-1] = arr[num2-1]
arr[num2-1] = temp
for i in range(len(arr)):
    print(arr[i])