import requests
from tabulate import tabulate
import json

portfolio = []


print("Crypto Portfolio Tracker")
print("Type 'done' when you're finished.\n")

while True:
    coin = input("Enter the coin name, type 'done' to finish: ").lower()
    if coin == "done":
        break

    quantity_input = input(f"How much {coin} do you own? ")
    if (quantity_input).isdigit() != True:
        raise ValueError("Please enter a number")
        
   

    purchase_price_input = input(f"What was your purchase price per {coin} (in USD)? ")
    if (purchase_price_input).isdigit() != True:
        raise ValueError("Please enter a number")
        continue
    

    quantity = float(quantity_input)
    purchase_price = float(purchase_price_input)

    portfolio.append({
        "symbol": coin,
        "quantity": quantity,
        "purchase_price": purchase_price
    })
    

    





def get_current_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    data = response.json()
    if coin_id in data:
        return data[coin_id]["usd"]
    else:
        print(f"Could not get price for {coin_id}")
        return 0


def calculate_portfolio(portfolio):
    table = []
    total_value = 0

    for coin in portfolio:
        symbol = coin["symbol"]
        quantity = coin["quantity"]
        purchase_price = coin["purchase_price"]

        current_price = get_current_price(symbol)
        value = quantity * current_price
        total_value += value

        if purchase_price > 0:
            gain_percentage = ((current_price - purchase_price) / purchase_price) * 100
        else:
            gain_percentage = 0

        table.append([
            symbol.capitalize(),
            quantity,
            f"${purchase_price:,.2f}",
            f"${current_price:,.2f}",
            f"${value:,.2f}",
            f"{gain_percentage:.2f}%"
        ])

    print("\nCryptocurrency Portfolio:\n")
    headers = ["Coin", "quantity", "purchase price", "current price", "value", "gain/loss"]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print(f"\nTotal Portfolio = ${total_value:,.2f}\n")





if __name__ == "__main__":
    calculate_portfolio(portfolio)