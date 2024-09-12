def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

try:
    original_price = float(input("Enter the original price of the item: R"))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    if final_price == original_price:
        print(f"No discount applied. The original price is: R{original_price:.2f}")
    else:
        print(f"The final price after applying the discount is: R{final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")
 