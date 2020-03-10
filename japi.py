import urllib.request
import json
import sys

#8024NLWI7ZUGQA7E
def getStockData(symbol) :
    symbol = symbol
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + symbol + "&apikey=8024NLWI7zUGQA7E"
    connection = urllib.request.urlopen(url)
    responseString = connection.read().decode()
    return responseString

def main():
    output = open("japi.out", "w+")

    for arg in sys.argv[1:]:
        arg = arg.upper()
        if arg == "QUIT":
            break
        else:
            print(getStockData(arg))
            output.write(getStockData(arg) + "\n")
            quote = json.loads(getStockData(arg))
            print("The current price of " + quote["Global Quote"]["01. symbol"] + " is: " + quote["Global Quote"]["05. price"])
            output.write("The current price of " + quote["Global Quote"]["01. symbol"] + " is: " + quote["Global Quote"]["05. price"] + "\n\n")
        
    while True:
        print("Enter a stock symbol or type quit to quit: ", end="")
        symbol = input().upper()
        if symbol == "QUIT":
            break
        else:
            print(getStockData(symbol))
            quote = json.loads(getStockData(symbol))
            print("The current price of " + quote["Global Quote"]["01. symbol"] + " is: " + quote["Global Quote"]["05. price"])

    output.close
    print("Stock Quotes retrieved successfully!")

if __name__ == "__main__":
    main()
