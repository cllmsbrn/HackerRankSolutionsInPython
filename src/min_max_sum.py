def min_max_sum(arr):
    print(sum(arr) - max(arr), end=" ")
    print(sum(arr) - min(arr))

if __name__ == "__main__":
    min_max_sum([1, 2, 3, 4, 5])