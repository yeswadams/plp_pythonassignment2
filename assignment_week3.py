def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
    else:
        final_price = price
    return final_price

original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount)

if final_price == original_price:
    print("No discount applied. Final price: $", final_price)
else:
    print("Final price after applying discount: $", final_price)