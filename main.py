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

                for stock in stockValue:
                    if stock[0] == stockName:
                        if int(amount) < stocks[1]:
                            accountBalance = accountBalance + ( stock[1] * int(amount) )
                            print(f"accountBalance is now {accountBalance}")

                            stocks[1] = int(stocks[1]) - int(amount)
                            print(f"you now have {stocks[1]} of {stocks[0]}")
                        elif int(amount) == stocks[1]:
                            accountBalance = accountBalance + ( stock[1] * int(amount) )
                            print(f"accountBalance is now {accountBalance}")
                            stockList.remove(stocks)
                        else:
                            print(f"you cannot sell {amount} of {stocks[0]}, as you only have {stocks[1]} {stocks[0]}")

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

    while True:
        action = input("Action: ")
        if action == "exit": break
        company = input("Company: ")
        if action == "evaluate": p.evaluate(company) ; continue
        amount = input ("Amount: ")
        match action:
            case "buy":
                p.buy(company, amount, stockList, accountBalance, stockValue)
                continue 
            case "sell":
                p.sell(company, amount, stockList, accountBalance, stockValue)
                continue
            case _:
                print("Not a valid action")
        break
    
    print(f"Stock list = {stockList}")


if __name__ == "__main__":
    main()
