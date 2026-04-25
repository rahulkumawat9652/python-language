bill_amount = float(input("enter bill amount "))
if bill_amount >=50000:
    discount = 30
elif bill_amount >= 40000 and bill_amount <50000:
    discount = 25
elif bill_amount >=30000 and bill_amount <40000:
    discount = 20
elif bill_amount >=20000 and bill_amount <30000:
    discount = 10
else:
    discount = 0
print("You got discount of ",discount)
find_bill = bill_amount - (bill_amount*discount/100)
print("your find bill is ",find_bill)