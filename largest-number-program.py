my_list = [23,45,67,45,67,89,34.7,56.9]
largest = 0
for i in range(0,len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print(largest)