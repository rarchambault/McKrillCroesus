import finance_client as fc
import json

START_DATE = "2023-01-01"
END_DATE = "2023-02-01"
TICKERS = ["AAL", "DAL", "UAL", "LUV", "HA"]

def optimal_ticker_combination(prices, initial_capital=1000000):
    days = len(prices)
    """
    Calculates the most optimal combination of tickers to buy and sell
    over a given number of days, given a set of stock prices for each day.

    Args:
    - prices (list of lists): A list of lists where each inner list
      represents the stock prices for a given day. Each inner list should
      have the same length, which should be the number of stocks being considered.
    - days (int): The number of days to simulate.
    - initial_capital (float): The amount of initial capital available to invest.

    Returns:
    - A list of tuples where each tuple represents a buy/sell transaction
      and has the format (ticker, buy_date, sell_date, profit).
    """

    # Step 1: Calculate the growth factor for each stock for every possible time interval
    growth_factors = [[1.0] * len(prices[0])]

    for i in range(1, days+1):
        growth_factor_day_i = [0.0] * len(prices[0])

        for j in range(len(prices[0])):
            max_growth_factor = 1.0

            for k in range(j, -1, -1):
                growth_factor_k_j = prices[i-1][j] / prices[i-1][k]
                max_growth_factor = max(max_growth_factor, growth_factors[i-1][k] * growth_factor_k_j)

            growth_factor_day_i[j] = max_growth_factor

        growth_factors.append(growth_factor_day_i)

    # Step 2: Calculate the optimal transactions using dynamic programming
    profits = [[0.0] * len(prices[0])]

    for i in range(1, days+1):
        profits_day_i = [0.0] * len(prices[0])

        for j in range(len(prices[0])):
            max_profit = 0.0

            for k in range(j, -1, -1):
                profit_k_j = initial_capital / prices[i-1][k] * growth_factors[i][j] - initial_capital
                if k > 0:
                    profit_k_j += profits[i-1][k-1]

                max_profit = max(max_profit, profit_k_j)

            profits_day_i[j] = max_profit

        profits.append(profits_day_i)

    # Step 3: Trace the optimal transactions
    optimal_transactions = []

    i = days
    j = len(prices[0]) - 1
    while i > 0 and j >= 0:
        for k in range(j, -1, -1):
            if profits[i][j] == initial_capital / prices[i-1][k] * growth_factors[i][j] - initial_capital + profits[i-1][k-1]:
                optimal_transactions.append(('Ticker ' + str(j+1), k+1, j+1, profits[i][j]))
                i -= 1
                j = k - 1
                break

    return list(reversed(optimal_transactions))


def getScore(growth, interval):
    return growth*(1/interval)

data = fc.getData(TICKERS, START_DATE, END_DATE)

moves = []

#transpose data list
data = {k: [dic[k] for dic in data] for k in data[0]}

# for ticker in TICKERS:
#     for i in data[ticker].keys():
#         for j in data[ticker].keys():
#             if i != j:
#                 profit = data[ticker][j] - data[ticker][i]
#                 moves.append({
#                     "ticker": ticker,
#                     "startDate": i,
#                     "endDate": j,
#                     "profit": profit
#                 })

print(optimal_ticker_combination(data, 1000000))


def optimal_ticker_combination(prices, initial_capital=1000000):
    days = len(prices)
    """
    Calculates the most optimal combination of tickers to buy and sell
    over a given number of days, given a set of stock prices for each day.

    Args:
    - prices (list of lists): A list of lists where each inner list
      represents the stock prices for a given day. Each inner list should
      have the same length, which should be the number of stocks being considered.
    - days (int): The number of days to simulate.
    - initial_capital (float): The amount of initial capital available to invest.

    Returns:
    - A list of tuples where each tuple represents a buy/sell transaction
      and has the format (ticker, buy_date, sell_date, profit).
    """

    # Step 1: Calculate the growth factor for each stock for every possible time interval
    growth_factors = [[1.0] * len(prices[0])]

    for i in range(1, days+1):
        growth_factor_day_i = [0.0] * len(prices[0])

        for j in range(len(prices[0])):
            max_growth_factor = 1.0

            for k in range(j, -1, -1):
                growth_factor_k_j = prices[i-1][j] / prices[i-1][k]
                max_growth_factor = max(max_growth_factor, growth_factors[i-1][k] * growth_factor_k_j)

            growth_factor_day_i[j] = max_growth_factor

        growth_factors.append(growth_factor_day_i)

    # Step 2: Calculate the optimal transactions using dynamic programming
    profits = [[0.0] * len(prices[0])]

    for i in range(1, days+1):
        profits_day_i = [0.0] * len(prices[0])

        for j in range(len(prices[0])):
            max_profit = 0.0

            for k in range(j, -1, -1):
                profit_k_j = initial_capital / prices[i-1][k] * growth_factors[i][j] - initial_capital
                if k > 0:
                    profit_k_j += profits[i-1][k-1]

                max_profit = max(max_profit, profit_k_j)

            profits_day_i[j] = max_profit

        profits.append(profits_day_i)

    # Step 3: Trace the optimal transactions
    optimal_transactions = []

    i = days
    j = len(prices[0]) - 1
    while i > 0 and j >= 0:
        for k in range(j, -1, -1):
            if profits[i][j] == initial_capital / prices[i-1][k] * growth_factors[i][j] - initial_capital + profits[i-1][k-1]:
                optimal_transactions.append(('Ticker ' + str(j+1), k+1, j+1, profits[i][j]))
                i -= 1
                j = k - 1
                break

    return list(reversed(optimal_transactions))

