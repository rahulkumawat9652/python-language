d1 = {"a":300,"b":400,"c":100}
d2 = {"a":300,"b":300,"c":500,"d":500}
result = {}
for k,v in d1.items():
    result[k] = v
for k,v in d2.items():
    if k in result:
        result[k] = result[k]+v 
    else:
        result[k] = v
print(result)
