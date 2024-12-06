def calculate_discount(price, discount_percent):

    discount_percent = discount_percent / 100

    if discount_percent  >= 0.2:
        Result = price - (price * discount_percent)
    else:
        Result = price

    return Result

price = int(input("Enter the original price: "))
discount = int(input("Enter the discount percent as a number offered: "))

print(calculate_discount(price, discount))