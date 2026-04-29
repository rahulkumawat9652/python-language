my_list = [23,45,67,45,67,89,34.7,56.9]
old = int(input("enteer odd number "))
new = int(input("enter new number "))
for i in range(0,len(my_list)):
    if my_list[i] == old:
        my_list[i] = new
print(my_list)