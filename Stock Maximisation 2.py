def stockmax(prices):

    prices_reversed = list(reversed(prices))
    n = len(prices_reversed)
    m = 0
    wallet = 0
    buy_sell = []
    
    for i in range(n):

        if prices_reversed[i] > m:
            m = prices_reversed[i]
            buy_sell += [1]
        else:
            wallet -= prices_reversed[i]
            wallet += m
            buy_sell += [0]

    return wallet
    

print stockmax([1, 3, 1, 2])
