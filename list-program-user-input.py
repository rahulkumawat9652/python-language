list_length = int(input("enter length"))
result = []
for i in range(0,list_length):
    num = int(input(f"enter value at position {i}"))
    result.append(num)
print(result)