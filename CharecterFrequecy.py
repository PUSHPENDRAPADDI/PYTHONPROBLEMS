# name = "google.com"
# for i in range(len(name)):


def char_frequency(str1):
dict = {}
for n in str1:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
    return dict
    
str1="sunny"
print(char_frequency('google.com'))
