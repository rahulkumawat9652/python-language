my_dict = {"name":"rahul","age":20,"gender":"male"}
print(my_dict)
r = my_dict.get("name")
print(r)
my_dict["age"] = 100
print(my_dict)
my_dict.update({"marks":99,"addres":"jaipur"})
print(my_dict)
del my_dict["gender"]
print(my_dict)
my_dict.pop("name")
print(my_dict)