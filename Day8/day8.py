if __name__ == "__main__":
    trees = [[0 for x in range(99)] for y in range(99)] #lazy to do the right thing

    # load data into trees
    with open("input.txt") as f:
        y = 0
        for line in f:
            line = line.strip()
            x = 0
            for c in line:
                trees[x][y] = int(c)
                x+=1
            y+=1

    # go through each tree
    length = x
    height = y
    visible = 0
    best = 0
    for y in range(height):
        for x in range(length):
            blocked = 0

            # Part1:check top visibility up to y
            for yy in range(y): #0 - y
                if trees[x][yy] >= trees[x][y]:
                    blocked += 1
                    break

            # Part2:check top visibility up to y
            top = 0
            for yy in range((y - 1), -1, -1):  # from y to top ,eg. 3-0
                if trees[x][yy] >= trees[x][y]:
                    top = y - yy
                    break
            if top == 0:
                top = y - 0

            # Part1:check bot visibility up to y
            for yy in range((height-1),y,-1): #height - y
                if trees[x][yy] >= trees[x][y]:
                    blocked += 1
                    break

            # Part2:check bot visibility up to y
            bot = 0
            for yy in range((y + 1), height, 1):  # from y to bot, eg 3-5
                if trees[x][yy] >= trees[x][y]:
                    bot = yy - y
                    break
            if bot == 0:
                bot = height - (y + 1)

            # Part1:check left visibility up to x
            for xx in range(x):  # 0 - x
                if trees[xx][y] >= trees[x][y]:
                    blocked += 1
                    break

            # Part2:check left visibility up to x
            left = 0
            for xx in range((x - 1), -1, -1):  # from x to left, eg 3-0
                if trees[xx][y] >= trees[x][y]:
                    left = x - xx
                    break
            if left == 0:
                left = x - 0

            # Part1:check right visibility up to x
            for xx in range((length - 1), x, -1):  # length - x
                if trees[xx][y] >= trees[x][y]:
                    blocked += 1
                    break

            # Part2:check right visibility up to x
            right = 0
            for xx in range((x + 1), length, 1):  # from x to right, eg 3-5
                if trees[xx][y] >= trees[x][y]:
                    right = xx - x
                    break
            if right == 0:
                right = left - (x + 1)

            # Part1
            if blocked < 4:
                visible += 1

            # Part2
            scenic = top * bot * left * right
            if scenic > best:
                best = scenic

    print(f"Day8 Part 1:{visible}")
    print(f"Day8 Part 2:{best}")
