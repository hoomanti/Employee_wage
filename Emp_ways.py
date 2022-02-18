import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 6
WORKING_DAY_PER_MONTH = 20
WORKING_HOUR_PER_MONTH = 100

day = 0
hour = 0
monthly_wage = 0
while (day < WORKING_DAY_PER_MONTH) and (hour < WORKING_HOUR_PER_MONTH):
    attendance = random.randint(0, 1)
    if attendance != 0:
        print("Employee is Full time")
        daily_wage = WAGE_PER_HOUR * FULL_DAY_HOUR
        hour += 8
    else:
        print("Employee is Part time")
        daily_wage = WAGE_PER_HOUR * PART_TIME_HOUR
        hour += 6

    print("Daily wage of the Employee:", daily_wage)
    day += 1
    monthly_wage = monthly_wage + daily_wage
print("Monthly wage is sum of above daily wages:", monthly_wage)
print("Total working days:", day)
print("Total working hours:", hour)
