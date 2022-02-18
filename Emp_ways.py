import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 6

attendance = random.randint(0, 2)
if attendance == 0:
    print("Employee is Absent")
    daily_wage = 0
elif attendance == 1:
    print("Employee is Part time")
    daily_wage = WAGE_PER_HOUR * PART_TIME_HOUR
else:
    print("Employee is Full time")
    daily_wage = WAGE_PER_HOUR * FULL_DAY_HOUR

print("Daily wage of the Employee:", daily_wage)

