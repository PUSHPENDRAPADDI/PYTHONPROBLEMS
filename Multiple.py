# arr = [[1,2,3], [], [2,3]]
# res = [ele for ele in arr if ele != []]
# print(str(res))        
arr = [1,2,3,4,5,6,7,8,9]
len = int(input("Enter length of array = "))
print("Enter elements of array = ")
mul = 1
for i in range(0,len):
    arr[i]= int(input())
    mul = mul * arr[i]
print(mul)