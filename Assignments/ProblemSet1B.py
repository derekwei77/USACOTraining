# Part A: House Hunting
annual_salary = int(input("Please input your starting annual salary (Dollar): "))
portion_saved = float(input("Please input the portion of salary to be saved: "))
total_cost = int(input("Please input the cost of your dream home (Dollar): "))
semi_annual_raise = float(input("Please input your semi-annual raise: "))

portion_down_payment = 0.25
annual_return = 0.04
current_savings = 0
target_saving = total_cost * portion_down_payment
number_of_months = 0
while (current_savings < target_saving):
    current_savings += annual_salary / 12 * portion_saved + current_savings * annual_return / 12
    # print(current_savings)
    number_of_months += 1
    if (number_of_months % 6 == 0):
        annual_salary *= 1 + semi_annual_raise

print('It takes ' + str(number_of_months) + ' months to save ' + str(target_saving) + 'K for your dream house')
