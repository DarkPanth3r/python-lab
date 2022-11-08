income = float(input("Enter the annual income: "))

#
# Write your code here.
#
if income < 85528:
    tax = (income * 0.18) - 556.2
    if tax < 0:
        tax = 0.0
else:
    surplus = (income - 85528) * 0.32
    tax = 14839 + surplus

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
