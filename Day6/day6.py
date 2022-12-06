if __name__ == "__main__":
    with open("input.txt") as f:
        buffer = []
        total = 0
        total1 = 0

        for line in f:
            for c in line:
                buffer.append(c)
                #part1
                if (len(set(buffer[-4:])) == 4 and total == 0):
                    total = len(buffer)

                #part2
                if (len(set(buffer[-14:])) == 14 and total1 == 0):
                    total1 = len(buffer)
                    break

    print(f"Day6 Part 1:{total}")
    print(f"Day6 Part 2:{total1}")