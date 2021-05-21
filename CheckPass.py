name = input("Enter name of student = ")
sub1 = int(input("Enter number of subject1 = "))
sub2 = int(input("Enter number of subject2 = "))
sub3 = int(input("Enter number of subject3 = "))
if sub1 < 33 or sub2< 33 or sub3 < 33:
    print(name," fail in specific subject try next year!")    
else:
    total = sub1+sub2+sub3
    percent = (total/300)*100
    if percent <40:
        print(name," failed ",percent,"% percentage overall")     
    else:
        print(name," passed with ",percent,"%")    