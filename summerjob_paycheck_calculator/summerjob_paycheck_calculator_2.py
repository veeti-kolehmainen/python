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