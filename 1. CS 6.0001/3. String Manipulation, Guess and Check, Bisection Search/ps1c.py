#Buying a house
#find ideal portion saved from annual salary

def total_savings(annual_salary, portion_saved):
    time_goal = 36
    monthly_salary = annual_salary/12
    semi_annual_raise = 0.07

    current_savings = 0
    r = 0.04

    time_months = 0
    while time_months < time_goal:
        current_savings = (portion_saved*monthly_salary + current_savings)*((r/12) + 1)
        time_months += 1
        if time_months % 6 == 0:
            monthly_salary += monthly_salary*semi_annual_raise
        
    return current_savings

def find_ideal_portion_saved(annual_salary):
    portion_saved = 0.5
    total_house_cost = 1000000
    portion_down_payment = 0.25*total_house_cost

    savings = total_savings(annual_salary, portion_saved)

    i = 0
    while abs(portion_down_payment - savings) > 100 :

        if (portion_down_payment - savings) > 0:
            portion_saved += 0.001

            savings = total_savings(annual_salary, portion_saved)

            i += 1

        else:
            portion_saved -= 0.001
            savings = total_savings(annual_salary, portion_saved)

            i += 1

        if i == 10000:
            break

    if portion_saved >= 1:
        print("You don't make enough money or your deadline is too close." )
    
    return portion_saved, i

annual_salary = float(input('Enter your starting annual salary:'))

best_savings_rate = find_ideal_portion_saved(annual_salary)[0]
steps = find_ideal_portion_saved(annual_salary)[1]

print('Best savings rate:', best_savings_rate)
print('Steps in bisection search:', steps)