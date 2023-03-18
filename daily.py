import finance_client as fc
import datetime as datetime

def getPeriodGreatest(tickers, startDate, endDate):
    data = fc.getData(tickers, "2023-01-01", "2023-02-01")

    maxgrowth = 0
    maxticker = ""
    for ticker in tickers:
        startPrice = float(data[ticker][startDate])
        endPrice = float(data[ticker][endDate])
        growth = endPrice/startPrice

        if (growth > maxgrowth):
            maxgrowth = growth
            maxticker = ticker
    
    return maxticker

def main():
    import datetime

    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 2, 1)

    delta = datetime.timedelta(days=1)

    while start_date < end_date:
        print(start_date.strftime('%Y-%m-%d'))
        start_date += delta

    
    tickers = ["AAL", "DAL", "UAL", "LUV", "HA"]
    print(getPeriodGreatest(tickers, "2023-01-10", "2023-01-11"))


if __name__ == "__main__":
    main()