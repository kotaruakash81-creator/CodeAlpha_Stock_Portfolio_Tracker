# CodeAlpha - Python Programming Task
# Stock Portfolio Tracker by Kotaru Akash
# Student ID: CA/DF1/300594

# Hardcoded stock prices (USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330,
    "AMZN": 3400,
    "INFY": 18,
    "TCS": 45
}

portfolio = {}
total_investment = 0

print("=== CodeAlpha Stock Portfolio Tracker ===")
print(f"Available Stocks: {', '.join(stock_prices.keys())}")
print("Type 'done' when finished\n")

# Taking user input
while True:
    stock_name = input("Enter Stock Name (e.g., AAPL): ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print(f"Stock {stock_name} not in our price list. Available: {list(stock_prices.keys())}")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        if quantity <= 0:
            print("Quantity must be > 0")
            continue
    except ValueError:
        print("Please enter a valid number!")
        continue

    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

    print(f"Added {quantity} shares of {stock_name}\n")

# Calculating total investment
print("\n--- Your Investment Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares x ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file (Task requirement)
save = input("\nDo you want to save report to file? (yes/no): ").lower()
if save == "yes":
    # Saving to TXT and CSV both
    with open("portfolio_report.txt", "w") as f:
        f.write("Stock Portfolio Report - CodeAlpha\n")
        f.write(f"Student: Kotaru Akash (CA/DF1/300594)\n\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
        f.write(f"\nTotal Investment: ${total_investment}\n")

    with open("portfolio_report.csv", "w") as f:
        f.write("Stock,Quantity,Price,Investment\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock]*qty}\n")
        f.write(f"TOTAL,,,{total_investment}\n")

    print("Reports saved as portfolio_report.txt and portfolio_report.csv")

print("\nTask Completed for CodeAlpha!")