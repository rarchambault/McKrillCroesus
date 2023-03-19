import finance_client as fc
import json

START_DATE = "2023-01-01"
END_DATE = "2023-02-01"
TICKERS = ["GOOG", "AMZN", "META", "MSFT", "AAPL"]

# def getPeriodGreatest(tickers, startDate, endDate, data):

#     maxgrowth = 0
#     maxticker = ""
#     for ticker in tickers:
#         startPrice = float(data[ticker][startDate])
#         endPrice = float(data[ticker][endDate])
#         growth = endPrice/startPrice

#         if (growth > maxgrowth):
#             maxgrowth = growth
#             maxticker = ticker
    
#     return maxticker



def getBestForInterval(interval, data):
    res = []
    startingIndex = 0
    revenue = 1000000
    while(startingIndex < len(data[TICKERS[0]])-1):
        endIndex = startingIndex + interval
        if (endIndex >= len(data[TICKERS[0]])):
            endIndex = len(data[TICKERS[0]]) - 1
        max = 0
        max_ticker = ""
        for ticker in TICKERS:
            starting = data[ticker][startingIndex]
            ending = data[ticker][endIndex]
            if (ending/starting > max):
                max = ending/starting
                max_ticker = ticker
        res.append({
            "date": str((data[max_ticker].keys())[startingIndex]).split(" ")[0],
            "action": "BUY",
            "ticker": max_ticker
        })
        res.append({
            "date": str((data[max_ticker].keys())[endIndex]).split(" ")[0],
            "action": "SELL",
            "ticker": max_ticker
        })
        revenue = revenue*max
        startingIndex = endIndex + 1
    return [res, revenue]

if __name__ == "__main__":
    data = fc.getData(TICKERS, START_DATE, END_DATE)
    max = 0
    max_res = []
    for i in range(1, 31):
        res = getBestForInterval(i, data)
        print(f"Interval {i} has {res[1]}")
        if (res[1] > max):
            max = res[1]
            max_res = res
    
    out_file = open("./results/results.json", "w")
    json.dump(max_res[0], out_file, indent = 6)
    out_file.close()







