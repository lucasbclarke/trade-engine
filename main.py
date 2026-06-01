account = [
    ["Alice", [40], [["SNPS", 40]] ],
    ["Terry", [60], [] ],
    ["Joy", [200], [] ]
]

userIndex = -1

class Portfolio:

    def buy(self, stockName, amount, stockValue, userAccount):
        accountBalance = userAccount[1]
        stockList = userAccount[2]

        print(f"purchased {amount} stock")
        foundStock = False
        
        for stocks in stockList:
            print(f"sotcks = {stocks}")
            if stockName in stocks:
                print(f"{stockName} is in stocklist")

                for stock in stockValue:
                    if stock[0] == stockName:
                        stockPrice = stock[1] * int(amount)
                        if accountBalance[0] < stockPrice:
                            print(f"Your accountBalance is only {accountBalance[0]} you can't buy {amount} stock with your current funds")
                        else:
                            accountBalance[0] -= stockPrice
                            stocks[1] = int(stocks[1]) + int(amount)
                            print(f"stock amount is now {stocks[1]}")
                            print(f"accountBalance is now {accountBalance[0]}")
                    break
                foundStock = True
                break
            break

        if not foundStock:
            print(f"{stockName} is not in stocklist")
            stockList.append([stockName, amount])
            for stock in stockValue:
                if stock[0] == stockName:
                    accountBalance[0] -= ( stock[1] * int(amount) )
                    print(f"accountBalance is now {accountBalance[0]}")

                break

    def sell(self, stockName, amount, stockValue, userAccount):
        accountBalance = userAccount[1]
        stockList = userAccount[2]

        print(f"sold {amount} stock")
        foundStock = False
        
        for stocks in stockList:
            if stockName in stocks:
                print(f"{stockName} is in stocklist")

                for stock in stockValue:
                    if stock[0] == stockName:
                        if int(amount) < stocks[1]:
                            accountBalance[0] += ( stock[1] * int(amount) )
                            print(f"accountBalance is now {accountBalance[0]}")

                            stocks[1] = int(stocks[1]) - int(amount)
                            print(f"you now have {stocks[1]} of {stocks[0]}")
                        elif int(amount) == stocks[1]:
                            accountBalance[0] += ( stock[1] * int(amount) )
                            print(f"accountBalance is now {accountBalance[0]}")
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

    while True:
        user = input("Who are you?: ")
        action = input("Action: ")
        if action == "exit": break
        company = input("Company: ")
        if action == "evaluate": p.evaluate(company) ; continue
        amount = input ("Amount: ")
        
        i = 0
        for users in account:
            print(f"user is {user} and users[0] is {users[0]}")
            if user == users[0]:
                userIndex = i
                break
            i += 1

        if userIndex < 0:
            print(f"{user} is not an account holder")
        
        else:
            match action:
                case "buy":
                    p.buy(company, amount, stockValue, account[userIndex])
                    continue 
                case "sell":
                    p.sell(company, amount, stockValue, account[userIndex])
                    continue
                case _:
                    print("Not a valid action")
            break
    
    print(f"Stock list = {stockList}")


if __name__ == "__main__":
    main()
