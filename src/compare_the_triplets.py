def compare_the_triplets(a, b):
    score_a = 0
    score_b = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1

    return score_a, score_b

if __name__ == "__main__":
    triplet_a = (5, 6, 7)
    triplet_b = (3, 6, 10)
    result = compare_the_triplets(triplet_a, triplet_b)
    print(result)