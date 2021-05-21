sen = input("Enter sentence = ")
sen = sen + " "
wd = ""
wdm = ""
max = ""
min = "pushpendghjkrayadva"
for i in range(len(sen)):
    ch2 = sen[i]
    ch = ord(ch2)
    if ch != 32:
        wd = wd + ch2
        wdm = wdm + ch2
    else:
        if (len(wd) > len(max)):
            max = wd
        wd = ""
        if (len(wdm) < len(min)):
            min = wdm
        wdm = ""
print(max," is largest word")
print(len(max)," is max length")
print(min," is smallest word")
print(len(min)," is min length")