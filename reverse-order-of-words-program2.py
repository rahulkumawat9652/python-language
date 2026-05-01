my_string = "python is good"
words = my_string.split()
words = words[ : :-1]
result = " ".join(words)
print(result)