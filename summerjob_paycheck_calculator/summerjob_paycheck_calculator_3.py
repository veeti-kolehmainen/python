# This is a paycheck calculator for my newspaper and advertisement delivery summerjob
# I did not calcualate taxes because I do not make over 10 000€ yearly


# Paycheck details in my contract
first_product = 16.89
next_products = 2.20
km_coverage = 7.80
extras = first_product + km_coverage

# Variables for the while loop
i = 1
total_pay = 0
week_number = 1

# While loop that calculates my paycheck
while i <= 4:
    pay = int(input("Week " + str(week_number) + " product amount: "))
    if(pay):
        pay = (pay - 1) * next_products + extras
        total_pay = total_pay + pay
    i += 1
    week_number += 1

bonus = input("Did you get any bonus money? If so, how much?: ")

if bonus == "no":
    total_pay = total_pay
else:
    total_pay = total_pay + float(bonus)

# Prints the total paycheck
print("Your paycheck should be: " + str(total_pay) + "€")