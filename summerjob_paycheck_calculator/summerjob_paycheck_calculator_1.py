# This is a paycheck calculator for my newspaper and advertisement delivery summerjob
# I did not calcualate taxes because I do not make over 10 000€ yearly


# Paycheck details in my contract
first_product = 16.89
next_products = 2.20
km_coverage = 7.80
extras = first_product + km_coverage


# Calculating the pay from week 1
week_1_pay = int(input("Week 1 product amount: "))
week_1_pay = (week_1_pay - 1) * next_products + first_product + km_coverage

# Calculating the pay from week 2
week_2_pay = int(input("Week 2 product amount: "))
week_2_pay = (week_2_pay - 1) * next_products + first_product + km_coverage

# Calculating the pay from week 3
week_3_pay = int(input("Week 3 product amount: "))
week_3_pay = (week_3_pay - 1) * next_products + first_product + km_coverage

# Calculating the pay from week 4
week_4_pay = int(input("Week 4 product amount: "))
week_4_pay = (week_4_pay - 1) * next_products + first_product + km_coverage

# Each week added together into one variable as a string
total_pay = str(week_1_pay + week_2_pay + week_3_pay + week_4_pay)

# Prints the total amount
print("Your paycheck should be: " + total_pay + "€")