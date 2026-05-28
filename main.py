import sys

class Portfolio:

    def buy(self, stockName, amount, stockList, accountBalance):
        print(f"purchased {amount} stock")
        foundStock = False
        
        for stocks in stockList:
            if stockName in stocks:
                print(f"{stockName} is in stocklist")
                stocks[1] = int(stocks[1]) + int(amount)
                print(f"stock amount is now {stocks[1]}")

                accountBalance = accountBalance - stocks[2]
                print(f"accountBalance is now {accountBalance}")

                # update stocklist with purchased amount
                foundStock = True
                break
        if not foundStock:
            print(f"{stockName} is not in stocklist")
            stockList.append([stockName, amount])


    #increase account balance when a stock is sold
    def sell(self, stock, quantity, stockList, accountBalance):
        print(f"sold {quantity} stock")
        foundStock = False
        
        for stocks in stockList:
            if stock in stocks:
                print(f"{stock} is in stocklist")
                # update stocklist with stock sold
                foundStock = True
                break
        if not foundStock:
            print(f"{stock} is not in stocklist and cannot be sold")

    def evaluate(self, company):
        # work out the value of the company somehow
        value = 0
        print(f"Value of {company} is {value}")

def main():
    p = Portfolio()
    action = sys.argv[1]
    company = sys.argv[2]
    amount = sys.argv[3]
    
    stockValue = [
            ["SNPS", 10],
            ["HLIX", 20],
            ["VNDG", 30],
            ["AEGS", 40], 
            ["VCTR", 50], 
            ["AVEN", 60] 
    ]

    # Mr Pike, can I assume (very simply) that 10 is the value of the stock, (even though stocks do not have a fixed price, but change based on supply and demand?)
    stockList = [["SNPS", 40, 10]] # remove the 10 and change the buy method to use the stockValue list
    #stockList = []

    accountBalance = 100 # this could be changed into a list if one "user" can have multiple accounts
    
    # change this so that the user does not perform one action and then the program exists, update it so the user can buy, sell and evaluate multiple times in one running session
    match action:
        case "buy":
            p.buy(company, amount, stockList, accountBalance)
        case "sell":
            p.sell(company, amount, stockList, accountBalance)
        case "evaluate":
            p.evaluate(company)
        case _:
            print("Not a valid action")

    print(f"Stock list = {stockList}")


if __name__ == "__main__":
    main()
