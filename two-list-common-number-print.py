list1 = [1,2,9,10,7,8]
list2 = [9,10,11,2,1,13]
result = []
for num in list1:
    if num in list2:
        result.append(num)
print(result)