def birthday_cake_candles(arr):
    tallest_candle_height = max(arr)
    return arr.count(tallest_candle_height)

if __name__ == "__main__":
    arr = [3, 2, 1, 3]
    result = birthday_cake_candles(arr)
    print(result)