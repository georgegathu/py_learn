#IF STATEMENTS

#Write a program:
# if good credit
#   put down 10% 
# otherwise 
#   put down 20% 
# print the down payment

property_price = 100000
good_credit = False

if good_credit:
    down_payment = 0.1 * property_price
else:
    down_payment = 0.2 * property_price
print(f"Down payment: ksh{down_payment}")



