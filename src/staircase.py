def staircase(n):
    space = " "
    octothorpe = "#"

    for i in range(n):
        for j in range(n - i - 1):
            print(space, end="")
        for k in range(i + 1):
            print(octothorpe, end="")
        print()

if __name__ == "__main__":
    staircase(6)