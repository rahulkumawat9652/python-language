num1 = int(input("enter number 1 "))
num2 = int(input("enter number 2 "))
num3 = int(input("enter number 3 "))
num4 = int(input("enter number 4 "))
if num1<num2 and num1<num3 and num1<num4:
    print("number 1 is smallest")
elif num2<num1 and num2<num3 and num2<num4:
    print("number 2 is smallest")
elif num3<num1 and num3<num2 and num3<num4:
    print("number 3 is smallest")
else:
    print("number 4 is smallest")