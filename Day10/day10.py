x = 1

class instruction:
    def __init__(self, num):
        self.cycle = 2
        self.num = num

    def tick(self):
        self.cycle -= 1
        if self.cycle == 0:
            global x
            x += self.num

class clock:
    def __init__(self, cycle):
        self.cycle = cycle
        self.total = 0
        self.picture = ""
        self.screenw = 40
        self.screenh = 6

    def tick(self):
        global x
        self.draw()
        self.cycle += 1
        # part1
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.total += self.cycle * x


    def draw(self):
        global x
        # part2
        if self.cycle % 40 == 0:
            self.picture += f"{self.cycle}\n"
        if self.cycle % 40 in [x - 1, x, x + 1]:
            self.picture += "#"
        else:
            self.picture += "."

if __name__ == "__main__":
    with open("input.txt") as f:
        clk = clock(0)
        # go through all instructions given
        for line in f:
            line = line.strip()
            clk.tick()
            if line and line != "noop":
                i = instruction(int(line.split()[1]))
                i.tick()
                clk.tick()
                i.tick()

    print(f"Day10 Part 1:{clk.total}")
    print(f"Day10 Part 2:{clk.picture}")
