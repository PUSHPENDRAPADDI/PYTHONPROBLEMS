def Fibonacii(n):
    if n <0:
        print("Incorrect Input")
    # elif n==1:
    #     return 0
    # or
    # elif n==2:
    #     return 1
    if n ==1 or n==2:
        return n-1
    else:
        return Fibonacii(n-1) + Fibonacii(n-2)
num = int(input("Enter the number for fibonacii = "))        
print("Fibonacii number is ", Fibonacii(num))