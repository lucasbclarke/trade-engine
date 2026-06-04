# include an abstract TradingStrategy class with an abstract check_signal() method --- Ask claude to go into more detail about this
# to incorporate inheritance, include MovingAverageStrategy, RSIStrategy, and RandomStrategy classes that inherit from the TradingStrategy class
# if two or more of these sub-classes have the same method check_signal() and behave different with each call then this is polymorphism 

# to include encapsulation in the project change this account list to be its own class with attributes such as name, balance and holdings that can only be changed through methods
class Account:
    def __init__(self, name, cash_balance, holdings):
         self.name = name
         self.cash_balance = cash_balance
         self.holdings = holdings
         
    def add_funds(self, amount):
        self.cash_balance += amount

    def deduct_funds(self, amount):
        self.cash_balance -= amount

    def add_to_holdings(self, stock):
        self.holdings.append(stock)



user_index = -1

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
            user_account.add_to_holdings([stock_name, amount])

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

    def evaluate(self, company):
        # work out the value of the company somehow
        value = 0
        print(f"Value of {company} is {value}")

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

    while True:
        User.name = input("Who are you?: ")
        action = input("Action: ")
        if action == "exit": break
        company = input("Company: ")
        if action == "evaluate": p.evaluate(company) ; continue
        amount = input ("Amount: ")
        
        match action:
            case "buy":
                p.buy(company, amount, stock_value, User)
                continue 
            case "sell":
                p.sell(company, amount, stock_value, User)
                continue
            case _:
                print("Not a valid action")
        break
    

if __name__ == "__main__":
    main()
