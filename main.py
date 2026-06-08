from abc import ABC, abstractmethod
from random import randint

class Account:
    def __init__(self, name, cash_balance, holdings):
         self.name = name
         self.cash_balance = cash_balance
         self.holdings = holdings
         
    def add_funds(self, amount):
        self.cash_balance = round(self.cash_balance + amount, 2)

    def deduct_funds(self, amount):
        self.cash_balance = round(self.cash_balance - amount, 2)

    def add_to_holdings(self, stock):
        self.holdings.append(stock)


class Portfolio:

    def buy(self, stock_name, amount, stock_value, user_account):
        account_balance = user_account.cash_balance
        stock_list = user_account.holdings

        print(f"purchased {amount} stock")
        found_stock = False
        
        for stocks in stock_list:
            if stock_name in stocks:
                print(f"{stock_name} is in stocklist")
                for stock in stock_value:
                    if stock[0] == stock_name:
                        #the price of the stock rises when it is bought
                        stock[1] = round(stock[1] * (1 + 0.02 * int(amount)), 2)

                        stock_price = stock[1] * int(amount)
                        if user_account.cash_balance < stock_price:
                            print(f"Your account_balance is only {account_balance} you can't buy {amount} stock with your current funds")
                        else:
                            user_account.deduct_funds(stock_price)
                            stocks[1] = int(stocks[1]) + int(amount)
                            print(f"stock amount is now {stocks[1]}")
                            print(f"account_balance is now {user_account.cash_balance}")
                        break
                found_stock = True

        if not found_stock:
            print(f"{stock_name} is not in stocklist")
            user_account.add_to_holdings([stock_name, int(amount)])

            for stock in stock_value:
                if stock[0] == stock_name:
                    if user_account.cash_balance < stock[1]:
                        print(f"Your balance is only {user_account.cash_balance}, you can't afford this")
                    else:
                        user_account.deduct_funds( stock[1] * int(amount) )
                        print(f"account_balance is now {user_account.cash_balance}")
                        break

    def sell(self, stock_name, amount, stock_value, user_account):
        account_balance = user_account.cash_balance
        stock_list = user_account.holdings

        print(f"sold {amount} stock")
        found_stock = False
        
        for stocks in stock_list:
            if stock_name in stocks:
                print(f"{stock_name} is in stocklist")

                for stock in stock_value:
                    if stock[0] == stock_name:
                        #the price of the stock falls when it is sold
                        stock[1] = round(stock[1] * (1 - 0.02 * int(amount)), 2)


                        if int(amount) < stocks[1]:
                            user_account.add_funds( stock[1] * int(amount) )
                            print(f"account_balance is now {user_account.cash_balance}")

                            stocks[1] = int(stocks[1]) - int(amount)
                            print(f"you now have {stocks[1]} of {stocks[0]}")
                        elif int(amount) == stocks[1]:
                            user_account.add_funds( stock[1] * int(amount) )
                            print(f"account_balance is now {account_balance}")

                            stock_list.remove(stocks)
                        else:
                            print(f"you cannot sell {amount} of {stocks[0]}, as you only have {stocks[1]} {stocks[0]}")

                found_stock = True
                break
        if not found_stock:
            print(f"{stock_name} is not in stocklist and cannot be sold")

    def update_prices(self, stock_value):
        import random
        for stock in stock_value:
            change = random.uniform(-0.05, 0.05)
            stock[1] = round(stock[1] * (1 + change), 2)

class TradingStragegy(ABC):
    @abstractmethod
    def check_signal(self):
        pass
    
    def check_strategy(self, company, stock_price, stock_value, User, portfolio):
        result = ""
        strategy = input("What strategy, random or threshold?: ")

        print(f"The chosen company is: {company}")
        match strategy:
            case "random":
                result = RandomStrategy().check_signal()

                match result:
                    case "buy":
                        max_affordable = User.cash_balance // stock_price
                        amount = randint(0, max_affordable) if max_affordable > 0 else 0
                        portfolio.buy(company, amount, stock_value, User)

                    case "sell":
                        current_holdings = 0
                        for holding in User.holdings:
                            if holding[0] == company:
                                current_holdings = holding[1]
                        amount = randint(0, current_holdings) if current_holdings > 0 else 0
                        portfolio.sell(company, amount, stock_value, User)

                    case "hold": 
                        pass
                    case _:
                        print("somehow there is another choice, which should not be possible")

                print(f"Strategy suggests: {result}")
            case "threshold":
                result = ThresholdStrategy().check_signal(stock_price, company, User)
                print(f"Strategy suggests: {result}")
            case _:
                print("Not a valid strategy")


class RandomStrategy(TradingStragegy):
    def check_signal(self):
        import random
        return random.choice(["buy", "sell", "hold"])

class ThresholdStrategy(TradingStragegy):
    def check_signal(self, stock_value, stock_name, user_account):
        if stock_value < 25:
            price_signal = "buy"
        elif stock_value > 50:
            price_signal = "sell"
        else:
            price_signal = "hold"

        if price_signal == "buy":
            if user_account.cash_balance < stock_value:
                return "hold"

        if price_signal == "sell":
            found_stock = False
            for holding in user_account.holdings:
                if holding[0] == stock_name:
                    found_stock = True
            if not found_stock:
                return "hold"

        return price_signal



def main():
    p = Portfolio()
    User = Account("", 120, [["SNPS", 40]])
    
    # the price of these stocks are currently fixed, in the future they should be dynamically scaled based on the evaluate function
    stock_value = [
            ["SNPS", 10],
            ["HLIX", 20],
            ["VNDG", 30],
            ["AEGS", 40], 
            ["VCTR", 50], 
            ["AVEN", 60] 
    ]
    
    Ts = RandomStrategy()
    accounts = {}
    while True:
        name = input("Who are you?: ")
        if name not in accounts:
            accounts[name] = Account(name, 120, []) 
        User = accounts[name]


        action = input("Action: ")
        if action == "exit": break

        if action == "print stock":
            print(f"{User.name} | Balance: {User.cash_balance}")
            print("Holdings:")
            for holding in User.holdings:
                for stock in stock_value:
                    if stock[0] == holding[0]:
                        total_value = round(stock[1] * holding[1], 2)
                        print(f"  {holding[0]}: {holding[1]} shares @ {stock[1]} = {total_value}")
            print("Market:")
            for stock in stock_value:
                owned = False
                for holding in User.holdings:
                    if holding[0] == stock[0]:
                        owned = True
                if not owned:
                    print(f"  {stock[0]}: {stock[1]}")
            print()
            continue

        if action == "strategy":
            company = input("Company: ")
            if company == "any":
                import random
                random_stock = random.choice(stock_value)
                Ts.check_strategy(random_stock[0], random_stock[1], stock_value, User, p)
            else:
                found_company = False
                for stock in stock_value:
                    if stock[0] == company:
                        Ts.check_strategy(company, stock[1], stock_value, User, p)
                        found_company = True
                        break
                if not found_company:
                    print("Not a valid company")
            p.update_prices(stock_value)
            print()
            continue

        company = input("Company: ")
        if action == "evaluate":
            p.evaluate(company) 
            p.update_prices(stock_value)
            print()
            continue

        amount = input ("Amount: ")
        
        match action:
            case "buy":
                p.buy(company, amount, stock_value, User)
                p.update_prices(stock_value)
                print()
                continue 
            case "sell":
                p.sell(company, amount, stock_value, User)
                p.update_prices(stock_value)
                print()
                continue
            case _:
                print("Not a valid action")
        break
    

if __name__ == "__main__":
    main()
