ch = input("Enter string for checking palindrome = ")
ch2 = ch[::-1]
if ch == ch2:
    print("Yes it is palindrome")
else:
    print("No it is not palindrome")