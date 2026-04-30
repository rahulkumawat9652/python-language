my_list = "abcd123"
count = 0
for ch in my_list:
    if ch.isalpha():
        count = count + 1
print(count)