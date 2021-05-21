sen = input("Enter sentence = ")
sen = sen+" "
wd = ""
for i in range(len(sen)):
    ch = sen[i]
    if ch != ' ':
        wd = wd + ch
    else:
        for j in range(len(wd)-1,-1,-1):
            print(wd[j],end='')
        print(end=" ")
        wd = ""