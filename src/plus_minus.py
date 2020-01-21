def plus_minus(arr):
    positives = 0
    negatives = 0
    zeros = 0

    for element in arr:
        if element > 0:
            positives += 1
        elif element < 0:
            negatives += 1
        else:
            zeros += 1

    positive_fractions = "{0:.6f}".format(positives / len(arr))
    negative_fractions = "{0:.6f}".format(negatives / len(arr))
    zero_fractions = "{0:.6f}".format(zeros / len(arr))

    return positive_fractions, negative_fractions, zero_fractions

if __name__ == "__main__":
    arr = [-4, 3, -9, 0, 4, 1]
    result = plus_minus(arr)
    print(result)