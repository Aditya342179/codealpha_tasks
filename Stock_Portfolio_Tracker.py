def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 2700,
        "MSFT": 300,
        "AMZN": 3300
    }

    portfolio = {}
    print("Enter your stock holdings. Type 'done' when finished.")

    while True:
        stock = input("Enter stock symbol (e.g., AAPL): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Please enter a valid stock symbol.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
            continue

        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

    if not portfolio:
        print("No stocks entered.")
        return

    total_investment = 0
    print("\nYour Portfolio:")
    print(f"{'Stock':<6} {'Quantity':<8} {'Price':<8} {'Value':<10}")
    print("-" * 35)
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        print(f"{stock:<6} {qty:<8} ${price:<7} ${value:<9}")

    print("-" * 35)
    print(f"Total Investment Value: ${total_investment}")

    save = input("Do you want to save this portfolio to a file? (yes/no): ").lower()
    if save == 'yes':
        filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
        try:
            with open(filename, 'w') as file:
                file.write("Stock,Quantity,Price,Value\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = price * qty
                    file.write(f"{stock},{qty},{price},{value}\n")
                file.write(f"\nTotal Investment Value,,,{total_investment}\n")
            print(f"Portfolio saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    stock_portfolio_tracker()