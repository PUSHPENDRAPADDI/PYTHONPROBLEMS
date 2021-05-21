age = int(input("Enter your age\n"))
if age in range(1,19):
    print("You are not allowed to Drive")
elif age in range(19,85):
    print("You are allowed to Drive")    
else:
    print("Please Enter valid Age or You are over Age!!!")    