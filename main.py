import sys

class Portfolio:

    def buy(self, stockName, amount, stockList, accountBalance, stockValue):
        while True:
            print(f"purchased {amount} stock")
            foundStock = False
        
            for stocks in stockList:
                if stockName in stocks:
                    print(f"{stockName} is in stocklist")
                    stocks[1] = int(stocks[1]) + int(amount)
                    print(f"stock amount is now {stocks[1]}")

                    for stock in stockValue:
                        if stock[0] == stockName:
                            accountBalance = accountBalance - ( stock[1] * int(amount) )
                            print(f"accountBalance is now {accountBalance}")
                            break

                    foundStock = True
                    break

            if not foundStock:
                print(f"{stockName} is not in stocklist")
                stockList.append([stockName, amount])
                for stock in stockValue:
                    if stock[0] == stockName:
                        accountBalance = accountBalance - ( stock[1] * int(amount) )
                        print(f"accountBalance is now {accountBalance}")

                break

    def sell(self, stockName, amount, stockList, accountBalance, stockValue):
        print(f"sold {amount} stock")
        foundStock = False
        
        for stocks in stockList:
            if stockName in stocks:
                print(f"{stockName} is in stocklist")
                stockList.remove(stocks)
                print(f"stock list is now {stockList}")


                for stock in stockValue:
                    if stock[0] == stockName:
                        accountBalance = accountBalance + ( stock[1] * int(amount) )
                        print(f"accountBalance is now {accountBalance}")

                foundStock = True
                break
        if not foundStock:
            print(f"{stockName} is not in stocklist and cannot be sold")

    def evaluate(self, company):
        # work out the value of the company somehow
        value = 0
        print(f"Value of {company} is {value}")

def main():
    p = Portfolio()
    action = sys.argv[1]
    company = sys.argv[2]
    amount = sys.argv[3]
    
    # the price of these stocks are currently fixed, in the future they should be dynamically scaled based on the evaluate function
    stockValue = [
            ["SNPS", 10],
            ["HLIX", 20],
            ["VNDG", 30],
            ["AEGS", 40], 
            ["VCTR", 50], 
            ["AVEN", 60] 
    ]

    stockList = [["SNPS", 40]] 

    accountBalance = 100 # this could be changed into a list if one "user" can have multiple accounts
    
    # change this so that the user does not perform one action and then the program exists, update it so the user can buy, sell and evaluate multiple times in one running session
    match action:
        case "buy":
            p.buy(company, amount, stockList, accountBalance, stockValue)
        case "sell":
            p.sell(company, amount, stockList, accountBalance, stockValue)
        case "evaluate":
            p.evaluate(company)
        case _:
            print("Not a valid action")

    print(f"Stock list = {stockList}")


if __name__ == "__main__":
    main()
