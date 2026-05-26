import sys

class Portfolio:

    def buy(self, stock, amount, stockList):
        print(f"purchased {amount} stock")
        found = False
        
        for stocks in stockList:
            if stock in stocks:
                print(f"{stock} is in stocklist")
                stocks[1] = int(stocks[1]) + int(amount)
                print(f"stock amount is now {stocks[1]}")

                # update stocklist with purchased amount
                found = True
                break
        if not found:
            print(f"{stock} is not in stocklist")
            stockList.append([stock, amount])


    def sell(self, stock, quantity, stockList):
        print(f"sold {quantity} stock")
        found = False
        
        for stocks in stockList:
            if stock in stocks:
                print(f"{stock} is in stocklist")
                # update stocklist with stock sold
                found = True
                break
        if not found:
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

    stockList = [["SNPS", 40]]
    #stockList = []
    
    match action:
        case "buy":
            p.buy(company, amount, stockList)
        case "sell":
            p.sell(company, amount, stockList)
        case "evaluate":
            p.evaluate(company)
        case _:
            print("Not a valid action")

    print(f"Stock list = {stockList}")


if __name__ == "__main__":
    main()
