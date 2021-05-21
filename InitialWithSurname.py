sen = input("Enter your name = ")
wd=""
for i in range(len(sen)):
    ch2 = sen[i]
    ch = ord(ch2)
    if ch != 32:
        wd = wd+ch2
    else:
        print(wd[0],end=".")
        wd = ""
print(wd)
