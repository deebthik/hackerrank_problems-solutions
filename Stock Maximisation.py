def stockmax(prices):

    prices_reversed = list(reversed(prices))
    n = len(prices_reversed)
    m = 0
    profit = 0
    buy_sell = []
    
    for i in range(n):

        if prices_reversed[i] > m:
            m = prices_reversed[i]
            buy_sell += [1]
        else:
            buy_sell += [0]

    wallet = 100000
    by = list(reversed(buy_sell))
    stocks = 0
    
    for i in range(n):
        if by[i] == 0:
            wallet -= prices[i]
            stocks += 1
        else:
            wallet += stocks * prices[i]
            stocks = 0
            

    return wallet-100000

print stockmax([1, 3, 1, 2])
