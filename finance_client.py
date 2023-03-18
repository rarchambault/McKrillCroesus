import yfinance as yf


def getData(string, startDate, endDate):
    data = {}
    for i in string:
        data[i] = yf.download(i, start=startDate, end=endDate, ignore_tz=False)
    return data 


