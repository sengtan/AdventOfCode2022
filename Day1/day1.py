
if __name__ == "__main__":
    with open("input.txt") as f:
        largest = 0
        cumulative = 0
        allelves = []
        for line in f:
            if line != "\n":
                cumulative += int(line)
            else:
                allelves.append(cumulative)
                largest = cumulative if cumulative > largest else largest
                cumulative = 0

    allelves.sort(reverse=True)
    print(f"Day1 Part 1:{largest}")
    print(f"Day1 Part 2:{sum([allelves[0],allelves[1],allelves[2]])}")