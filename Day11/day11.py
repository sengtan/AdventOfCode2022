items = {}
itemz = {}
reducer = 1

class monkey:
    def __init__(self, number, starting, operation, divby, t, f):
        global items, itemz
        items[number] = starting.copy()
        itemz[number] = starting.copy()
        self.number = number
        self.operation = operation
        self.divby = divby
        self.t = t
        self.f = f
        self.inspected = 0
        self.inspectedz = 0

    def turn(self):
        global items, reducer
        starting = items[self.number]
        for item in starting:
            new = self.operation(item)//3
            if new % self.divby == 0:
                items[self.t].append(new % reducer)
            else:
                items[self.f].append(new % reducer)
            self.inspected += 1
        items[self.number] = []

    def turnz(self):
        global itemz, reducer
        starting = itemz[self.number]
        for item in starting:
            new = self.operation(item)
            if new % self.divby == 0:
                itemz[self.t].append(new % reducer)
            else:
                itemz[self.f].append(new % reducer)
            self.inspectedz += 1
        itemz[self.number] = []

if __name__ == "__main__":
    monkeys = [
        monkey(0, [62, 92, 50, 63, 62, 93, 73, 50], lambda x: x * 7, 2, 7, 1),
        monkey(1, [51, 97, 74, 84, 99], lambda x: x + 3, 7, 2, 4),
        monkey(2, [98, 86, 62, 76, 51, 81, 95], lambda x: x + 4, 13, 5, 4),
        monkey(3, [53, 95, 50, 85, 83, 72], lambda x: x + 5, 19, 6, 0),
        monkey(4, [59, 60, 63, 71], lambda x: x * 5, 11, 5, 3),
        monkey(5, [92, 65], lambda x: x * x, 5, 6, 3),
        monkey(6, [78], lambda x: x + 8, 3, 0, 7),
        monkey(7, [84, 93, 54], lambda x: x + 1, 17, 2, 1),
    ]

    round = 0
    limit = 20
    limitz = 10000
    active = []
    activez = []

    for mon in monkeys:
        reducer *= mon.divby

    while round != limitz:
        for mon in monkeys:
            mon.turn()
            mon.turnz()
        round += 1
        if round == limit:
            for i, mon in enumerate(monkeys):
                active.append(mon.inspected)
                print(f"Monkey {i}: {items[i]}")
            active.sort(reverse=True)

    for i, mon in enumerate(monkeys):
        activez.append(mon.inspectedz)
        print(f"Monkey {i}: {itemz[i]}")
    activez.sort(reverse=True)

    print(f"Day11 Part 1:{active[0]*active[1]}")
    print(f"Day11 Part 2:{activez[0]*activez[1]}")
