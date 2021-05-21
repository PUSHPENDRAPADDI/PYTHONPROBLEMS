name = input("Enter your name ")
num = int(input("Enter place you want to remove = "))
for i in range(len(name)):
    if (i == num):
        pass
    else:
        print(name[i],end="")
