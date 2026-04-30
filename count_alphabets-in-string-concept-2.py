my_list = "abcd123"
count = 0
for ch in my_list:
    ascii = ord(ch)
    if(ascii>=65 and ascii<=98) or (ascii>=97 and ascii<=122):
        count = count + 1
print(count)