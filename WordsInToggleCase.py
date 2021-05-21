# sen = input("Enter sentence = ")
sen = "puShPENdra"
sen = sen+" "
wd = ""
ch2='r'
for i in range(len(sen)):
    ch = sen[i]
    if ch != ' ':
        if ord(ch) >=65 and ord(ch) <=90:
            ch2= ord(ch)+32
            print(ch2)
    # else:
    #     print(wd.title(),end=' ')
    #     wd=""