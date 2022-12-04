if __name__ == "__main__":
    with open("input.txt") as f:
        total = 0
        total1 = 0
        for line in f:
            a, b = line.split(',')
            a = [int(x) for x in a.split('-')]
            b = [int(x) for x in b.split('-')]
            if (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1]):
                total += 1

            if (a[0] <= b[0] <= a[1]) or (b[0] <= a[0] <= b[1]):
                total1 += 1


    print(f"Day4 Part 1:{total}")
    print(f"Day4 Part 2:{total1}")