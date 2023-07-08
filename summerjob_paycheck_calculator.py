# This is a paycheck calculator for my newspaper and advertisement delivery summerjob
# I did not calcualate taxes because I do not make over 10 000€ yearly


# Paycheck details in my contract
first_product = 16.89
next_products = 2.20
km_coverage = 7.80
extras = first_product + km_coverage


# Function for calculating a week's payment
def calculate_weekly_payment(week_var_name, week_number):
    week_var_name = int(input("Week " + week_number + " product amount: "))
    week_var_name = (week_var_name - 1) * next_products + extras
    return week_var_name

# Calling the function with 4 different weeks
week_1_pay = calculate_weekly_payment("week1", "1")
week_2_pay = calculate_weekly_payment("week2", "2")
week_3_pay = calculate_weekly_payment("week3", "3")
week_4_pay = calculate_weekly_payment("week4", "4")

# Adding all the weeks together and printing the total paycheck
total_payment = week_1_pay + week_2_pay + week_3_pay + week_4_pay
print("Your paycheck should be: " + str(total_payment) + "€")



# Old version that I made before I learned functions

# Calculating the pay from week 1
# week_1_pay = int(input("Week 1 product amount: "))
# week_1_pay = (week_1_pay - 1) * next_products + first_product + km_coverage

# Calculating the pay from week 2
# week_2_pay = int(input("Week 2 product amount: "))
# week_2_pay = (week_2_pay - 1) * next_products + first_product + km_coverage

# Calculating the pay from week 3
# week_3_pay = int(input("Week 3 product amount: "))
# week_3_pay = (week_3_pay - 1) * next_products + first_product + km_coverage

# Calculating the pay from week 4
# week_4_pay = int(input("Week 4 product amount: "))
# week_4_pay = (week_4_pay - 1) * next_products + first_product + km_coverage

# Each week added together into one variable as a string
# total_pay = str(week_1_pay + week_2_pay + week_3_pay + week_4_pay)

# Prints the total amount
# print("Your paycheck should be: " + total_pay + "€")