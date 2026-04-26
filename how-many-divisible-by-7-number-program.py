num1 = int(input("enter starting number  "))
num2 = int(input("enter last number "))
i = num1
count  = 0
while i<=num2:
    if i%7 == 0:
        count = count + 1
    i = i+1
print(count)