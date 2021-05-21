sen = input("Enter sentence = ")
w = input("Enter word = ")
sen = sen + " "
wd = ""
f = 0
for i in range(len(sen)):
    ch = sen[i]
    if ch != ' ':
        wd = wd + ch
    else:
        if wd == w:
            f=f+1
        wd = ""
print("frequency is ",f)