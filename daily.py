import datetime
import yfinance as yf

def getDailyInfo(str ticker, datetime start, datetime end):
    var data = yf.download(ticker, str(start), str(end))




def main()
    startDate = datetime.datetime(2023, 1, 1)
    endDate = datetime.datetime(2023, 2, 1)
    getDailyInfo("AAL", startDate, endDate)
    getDailyInfo("DAL", startDate, endDate)
    getDailyInfo("UAL", startDate, endDate)
    getDailyInfo("LUV", startDate, endDate)
    getDailyInfo("HA", startDate, endDate)