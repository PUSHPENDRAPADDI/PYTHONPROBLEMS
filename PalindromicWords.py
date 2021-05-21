sen = input("Enter sentence =")
sen = sen + " "
wd = ""
wd2 = ""
f = 0
for i in range(len(sen)):
    ch = sen[i]
    if ch != ' ':
        wd = wd + ch
        wd2 = wd2 + ch
    else:
        for j in range(len(wd)-1,-1,-1):
            wd2= wd[::-1]
        if wd == wd2:
            print(wd2,end=',')
        wd = ''