my_string = "asdfASDF"
lower_count = 0
upper_count = 0
for ch in my_string:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
print(upper_count)
print(lower_count)