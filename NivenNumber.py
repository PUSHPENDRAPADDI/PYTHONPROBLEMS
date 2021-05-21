num = int(input("Enter number for checking NivenNumber = "))
num2= 0
numO= num
while numO!=0:
    temp = numO%10
    num2 = num2+temp
    numO = numO//10
if num%num2==0:
    print("It is NivenNumber")
else:
    print("It is not a NivenNumber")