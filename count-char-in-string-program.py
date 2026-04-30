my_string = input("enter a string = ")
result = {}
for ch in my_string:
    if ch in result:
        result[ch] += 1
    else:
        result[ch] = 1
print(result)