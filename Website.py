web = input("Enter your website = ")
if web.endswith(".com"):
    print("Comercial Website")
elif web.endswith(".in"):
    print("Indian Website")
elif web.endswith(".org"):
    print("Organisational Website")
else :
    print("Your personal Website")