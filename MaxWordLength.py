sen = input("Enter sentence = ")
sen = sen + " "
wd = ""
max = ""
Cs = 0
Cw = 0
for i in range(len(sen)):
    ch2 = sen[i]
    ch = ord(ch2)
    if ch != 32:
        wd = wd + ch2
    else:
        if len(wd) > len(max):
            max = wd
        wd = ""
print(max," is largest word")
print(len(max)," is max length")