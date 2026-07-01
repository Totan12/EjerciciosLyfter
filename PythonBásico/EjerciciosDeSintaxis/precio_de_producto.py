price = float(input("Enter the price: "))
if price < 100:
    price *= 0.98
else:
    price *= 0.9
price = round(price, 2)
print(f"Total price: {price}")
