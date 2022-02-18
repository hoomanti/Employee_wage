import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8

attendance = random.randint(0, 1)
if attendance == 0:
    print("Employee is Absent")
    daily_wage = 0
else:
    print("Employee is Present")
    daily_wage = WAGE_PER_HOUR * FULL_DAY_HOUR

print("Daily wage of the Employee:", daily_wage)

