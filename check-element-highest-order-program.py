my_list = [5,1,4,"rahul",567.8,1,1,5]
result = []
for num in my_list:
    if num not in result:
        result.append(num)
highest_number = 0
highest_element = 0
for num in result:
    c = my_list.count(num)
    print(f"{num} occurs {c} time")
    if c > highest_element:
        highest_element = c
        highest_number = num
print(f"highest element = {highest_number}")