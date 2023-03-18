import finance_client as fc
import json

START_DATE = "2023-01-01"
END_DATE = "2023-02-01"
TICKERS = ["AAL", "DAL", "UAL", "LUV", "HA"]

data = fc.getData(TICKERS, START_DATE, END_DATE)


max = 0
max_ticker = ""

for i in data:
    starting = data[i][0]
    ending = data[i][-1]
    # print (f"{i} started at {starting} and ended at {ending}")
    # print (f"{i} return was {ending/starting}")
    if ending/starting > max:
        max = ending/starting
        max_ticker = i

res = []
res.append(
    {
        "date": str((data[max_ticker].keys())[0]).split(" ")[0],
        "action": "BUY",
        "ticker": max_ticker,
    }
)
res.append(
    {
        "date": str((data[max_ticker].keys())[-1]).split(" ")[0],
        "action": "SELL",
        "ticker": max_ticker,
    }
)

out_file = open("./results/dumb.json", "w")

json.dump(res, out_file, indent = 6)

out_file.close()