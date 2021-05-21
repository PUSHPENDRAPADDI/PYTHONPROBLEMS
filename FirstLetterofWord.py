sen = "Pushpendra yadav"
sen = " " + sen
for i in range(len(sen)):
    ch2 = sen[i]
    ch = ord(ch2)
    if ch == 32:
        print(sen[i+1], end=".")