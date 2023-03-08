import numpy as np

def StockPicker(prices):
    if len(prices) < 2:
        return -1
    else:

        price_diff = np.diff(prices)

        max_diff_index = np.argmax(price_diff)
        if price_diff[max_diff_index] > 0:

            return price_diff[max_diff_index]
        else:

            return -1

prices1 = [44, 30, 24, 32, 35, 30, 40, 38, 15]
prices2 = [10, 9, 8, 2]
prices3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(StockPicker(prices1)) 
print(StockPicker(prices2)) 
print(StockPicker(prices3))