num1 = int(input("enter starting number  "))
num2 = int(input("enter last number "))
i = num1
total  = 0
while i<=num2:
    if i%4 == 0:
        total = total + i
    i = i+1
print(total)
