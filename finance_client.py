import yfinance as yf


def getData(tickers, startDate, endDate):
    data = {}
    for i in tickers:
        data[i] = yf.download(i, start=startDate, end=endDate, ignore_tz=False)
        data[i] = data[i]["Open"]
    return data 


