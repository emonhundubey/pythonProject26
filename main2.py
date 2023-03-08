# from main import total

print("Welcome to Circle Phones’ Profit calculator")
time_period = {1: 1,
              2: 7,
              3: 5,
              4: 2}

total_profit = 0
while True:
    user_time_period = int(input("Enter product number 1-5 or 0 to stop: "))
    if user_time_period == 0:
        break
    day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")
    if user_time_period in time_period:
        user_quantity = int(input("Enter the quantity: "))
        total_profit += float(time_period[user_time_period]) * user_quantity
    else:
        break
print(f'Total Profit for the {day} is: {total_profit}')
,
