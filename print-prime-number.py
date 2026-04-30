list = [1,2,3,4,5,6,7,8]
for num in list:
    factors = 0
    for i in range(1,num+1):
        if num%i == 0:
            factors += 1
    if factors == 2:
         print(num)