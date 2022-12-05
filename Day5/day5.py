import copy

if __name__ == "__main__":
    with open("input.txt") as f:
        crates = {
            '1':['C','Z','N','B','M','W','Q','V'],
            '2':['H','Z','R','W','C','B'],
            '3':['F','Q','R','J'],
            '4':['Z','S','W','H','F','N','M','T'],
            '5':['G','F','W','L','N','Q','P'],
            '6':['L','P','W'],
            '7':['V','B','D','R','G','C','Q','J'],
            '8':['Z','Q','N','B','W'],
            '9':['H','L','F','C','G','T','J'],
        }

        a = copy.deepcopy(crates)
        b = copy.deepcopy(crates)

        output = ""
        output1 = ""

        for line in f:
            _,n,_,f,_,d = line.split()
            for i in range(int(n)):
                a[d].append(a[f].pop())

            b[d].extend(b[f][-int(n):])
            b[f] = b[f][:-int(n)]

        for i in range(9):
            output += a[str(i+1)][-1]
            output1 += b[str(i+1)][-1]

    print(f"Day5 Part 1:{output}")
    print(f"Day5 Part 2:{output1}")