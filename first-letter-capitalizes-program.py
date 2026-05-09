my_string = "python is good"
words = my_string.split()
result = " ".join(i.capitalize() for i in words)
print(result)