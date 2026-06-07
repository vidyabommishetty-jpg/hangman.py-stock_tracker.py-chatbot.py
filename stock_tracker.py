stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 350
}
stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))
if stock_name in stocks:
    total = stocks[stock_name] * quantity
    print("Total Investment =", total)
else:
    print("Stock not found")
with open("investment.txt", "w") as file:
    file.write(f"Total Investment = {total}")
