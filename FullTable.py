import time
def table(num):
    for i in range(1,num+1):
        print("!!!!-- Table of : ",i)
        for j in range(1,11):
            time.sleep(0.8)
            print(i," * ",j," = ",i*j)
num = int(input("Enter the number upto which you want table = "))            
table(num)        