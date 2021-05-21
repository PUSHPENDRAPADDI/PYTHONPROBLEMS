sen = input("Enter sentences = ")
Cs=0
Cw=0
for i in range(len(sen)):
    ch2 = sen[i]
    ch = ord(ch2)
    if ch == 32:
        Cs=Cs+1
    else:
        Cw=Cs+1
print(Cs," is Spaces")
print(Cw," is Words")