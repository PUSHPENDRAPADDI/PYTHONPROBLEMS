# name = input("Enter name of student = ")
num1 = int(input("Enter number of subject1 = "))
num2 = int(input("Enter number of subject2 = "))
num3 = int(input("Enter number of subject3 = "))
num4 = int(input("Enter number of subject4 = "))
num5 = int(input("Enter number of subject5 = "))
totalOb = (num1+num2+num3+num4+num5)
percentage = (totalOb/500)*100
if num1 >= num2 >= num3 >= num4 >= num5 >= 33:
    if percentage>=40:
        print("You are Passed with ",percentage,"%")
    elif percentage<40:
        print("You are Promoted with ",percentage,"%")
elif num1 < 33 or num2 < 33 or num3 < 33 or num4 <33 or num5 < 33:
    if percentage >= 40:
        print("You have less marks in subject and Promoted with percentage is ",percentage,"%")
    elif percentage<40:
        print("You are fail with percent = ",percentage)    