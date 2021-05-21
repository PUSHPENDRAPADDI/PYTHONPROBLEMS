# num = int(input("Enter number to check whether the number is pronic or not = "))
num = 20
flag = 0
for i in range(2,num//2):
    if num % i == 0 and num % i+1 ==0:
        print(i," Hai to ",num)
        flag = flag+1
    # else:
    #     print(i," hai to ",num)
if flag == 0:
    print("The number is not pronic")
else:
    print("The number is pronic")
    