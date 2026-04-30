my_list = [1,2,3,4,"rahul",5,6,7,8]
value = int(input("enter value "))
if value in my_list:
    index = my_list.index(value)
    print("index",index)
else:
    print("not in list")