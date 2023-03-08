print("Welcome to Circle Phones’ Profit calculator")

total = 0

prices = {'1': 120.45,
          '2': 9.50,
          '3': 75.79,
          '4': 65.73,
          '5': 51.49}

while True:
    user_product_number = input("Enter product number 1-5, or enter 0 to stop:")
    if user_product_number in prices:
        user_product_quantity = int((input("Enter quantity of products sold:")))
        total += float(prices[user_product_number]) * user_product_quantity
    elif user_product_number not in prices and user_product_number != '0':
        print('Invalid input, please enter a valid number')
    else:
        break
print("Your total is", total)

