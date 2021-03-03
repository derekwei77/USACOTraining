def calculateTotalSaving(annual_salary, portion_saved, number_of_months, annual_return):
    current_savings = 0

    number_of_months = 0
    while (number_of_months < 36):
        current_savings += annual_salary / 12 * portion_saved / 10000 + current_savings * annual_return / 12
        # print(current_savings)
        number_of_months += 1
        if (number_of_months % 6 == 0):
            annual_salary *= 1 + semi_annual_raise
    return current_savings 




annual_salary = int(input("Please input your starting annual salary (Dollar): "))
#portion_saved = float(input("Please input the portion of salary to be saved: "))
total_cost = 1000000
semi_annual_raise = 0.07

portion_down_payment = 0.25
annual_return = 0.04
target_saving = total_cost * portion_down_payment
print('target saving: ' + str(target_saving))

low = 0
high = 10000
best_saving_rate = int((low + high) / 2)
steps = 1
total_savings = calculateTotalSaving(annual_salary, best_saving_rate, 36, annual_return)
while (abs(total_savings - target_saving) > 100):
    if (total_savings > target_saving):
        high = best_saving_rate
        best_saving_rate = int((low + best_saving_rate) / 2)
    else:
        low = best_saving_rate
        best_saving_rate = int((best_saving_rate + high) / 2)
    total_savings = calculateTotalSaving(annual_salary, best_saving_rate, 36, annual_return)
    print('total saving: ' + str(total_savings) + ', saving rate: ' + str(best_saving_rate))
    steps += 1

print('Best savings rate: ' + str(best_saving_rate / 10000.0))
print('Steps in bisection search: ' + str(steps))