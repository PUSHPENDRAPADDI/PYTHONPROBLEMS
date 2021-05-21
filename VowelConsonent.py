sc = input("Enter sentence = ")
sc = sc.upper()
Cv=0
Cc=0
Cs=0
Cd=0
for i in range(0,len(sc)):
    ch = sc[i]
    x = ord(ch)
    if x>=65 and x<=90:
        if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
            Cv=Cv+1
        else:
            Cc=Cc+1
    elif x>=48 and x<=57:
        Cd=Cd+1
            
    else:
        Cs=Cs+1
print("No of Vowel ",Cv)
print("No of Consonent ",Cc)
print("No of digit ",Cd)
print("No of special charecter ",Cs)