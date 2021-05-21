num = int(input("Enter year for checking leap year = "))
if(num%4==0):
    if(num%100==0):
        if(num%400==0):
            print("Yes its leap year")
        else:
            print("No its not leap year")
    else:
        print("Yes its leap year")
else:
    print("No its not leap year")