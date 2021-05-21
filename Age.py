age = int(input("Enter your age\n"))
if age in range(1,13):
    print("You are child")
elif age in range(13,20):
    print("You are Teenager")    
else:
    print("You are a man")    