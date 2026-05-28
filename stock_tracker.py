# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total_investment = 0

print("Available Stocks:")
for stock in stock_prices:
    print(stock, ":", stock_prices[stock])

# Number of stocks user wants to enter
n = int(input("\nHow many stocks do you want to buy? "))

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Investment for", stock_name, "=", investment)

    else:
        print("Stock not available!")

print("\nTotal Investment Value =", total_investment)

# Save result to file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Result saved in portfolio.txt")