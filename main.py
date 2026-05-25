import sys

class Portfolio:

    def buy(self, stock, amount, stockList):
        print(f"purchased {amount} stock Synapse Therapeutics")
        found = False
        
        for stocks in stockList:
            if stock in stocks:
                print(f"{stock} is in stocklist")
                # update stocklist with purchased amount
                found = True
                break
        if not found:
            print(f"{stock} is not in stocklist")
            stockList.append([stock, amount])


        #match stock:
        #    case "SNPS":
        #        print(f"purchased {amount} stock Synapse Therapeutics")
        #        found = False
        #        for stocks in stockList:
        #            if stock in stocks:
        #                print("SNPS is in stocklist")
        #                # update stocklist with purchased amount
        #                found = True
        #                break

        #        if not found:
        #                print("SNPS is not in stocklist")
        #                stockList.append(["SNPS"])


        #    case "HLIX":                   
        #        print(f"purchased {amount} stock Helix Logistics")
        #    case "VNDG":                   
        #        print(f"purchased {amount} stock Vanguard Defense Group")
        #    case "AEGS":                   
        #        print(f"purchased {amount} stock Aegis Tactical Systems")
        #    case "VCTR":                   
        #        print(f"purchased {amount} stock Vector Freight")
        #    case "AVEN":                   
        #        print(f"purchased {amount} stock Aventine Global Syndicate")
        #    case _:
        #        print("not valid company")


    def sell(self, stock, amount):
        match stock:
            case "SNPS":
                print(f"purchased {amount} stock Synapse Therapeutics")
            case "HLIX":                   
                print(f"purchased {amount} stock Helix Logistics")
            case "VNDG":                   
                print(f"purchased {amount} stock Vanguard Defense Group")
            case "AEGS":                   
                print(f"purchased {amount} stock Aegis Tactical Systems")
            case "VCTR":                   
                print(f"purchased {amount} stock Vector Freight")
            case "AVEN":                   
                print(f"purchased {amount} stock Aventine Global Syndicate")
            case _:
                print("not valid company")

    def evaluate(self, company):
        # work out the value of the company somehow
        value = 0
        print(f"Value of {company} is {value}")



def main():
    p = Portfolio()
    action = sys.argv[1]
    company = sys.argv[2]
    amount = sys.argv[3]

    #stockList = [["SNPS", 40]]
    stockList = []
    
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
