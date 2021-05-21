sen = input("Enter sentence = ")
sen = sen+" "
wd = ""
for i in range(len(sen)):
    ch = sen[i]
    if ch != ' ':
        wd = wd+ch
    else:
        print(wd.title(),end=' ')
        wd=""