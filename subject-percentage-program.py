math = int(input("enter marks in math "))
science = int(input("enter marks in science "))
english = int(input("enter marks in english "))
hindi = int(input("enter marks in hindi "))
history = int(input("enter marks in history "))
total_marks = math + science + english + hindi +history
percentage = (total_marks /500)*100
print("percentage is ", percentage)
if percentage >= 90 and percentage <=100:
    print("A  gread")
elif percentage >= 80 and percentage <90:
    print("B gread")
elif percentage >= 70 and percentage <80:
    print("C gread")
elif percentage >= 60 and percentage <70:
    print("D gread")
elif percentage >= 1 and percentage <60:
    print("Fail")
else:
    print("Invalid percentage")