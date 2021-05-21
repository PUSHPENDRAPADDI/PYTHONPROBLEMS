arr = [1,2,3,4,5,6,7,8,9]
count=0
num = int(input("Enter element for searching = "))
for i in range(len(arr)):
    if num == arr[i]:
        count = count+1
        break
if count>0:
    print("The number is in list") 
else:
    print("The number is not in list")         