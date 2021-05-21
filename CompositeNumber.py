num = 4
num2 = num//2
div = 0
sum=0
for i in range(2,num2):
    if num%i==0:
        div=1
if div==1:
    print(num," is composite")
else:
    print(num," is not composite")