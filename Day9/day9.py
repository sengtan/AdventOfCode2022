if __name__ == "__main__":
    with open("input.txt") as f:
        # starting position of 0 - 9
        ropeh = {}  # 0 - 9
        n = 10  #num of nodes
        p1 = 1
        p2 = 9
        for i in range(n):
            ropeh[i] = [0, 0]

        # storage for tail travelled spots
        touched1 = set()
        touched2 = set()

        # go through all directions given
        for line in f:
            line = line.strip()

            x, y = 0, 0
            m, t = line.split()

            # get the direction of movement
            if m == 'R':
                x = 1
            elif m == "L":
                x = -1
            elif m == "U":
                y = 1
            elif m == "D":
                y = -1

            for _ in range(int(t)):
                # move head 0
                ropeh[0][0] += x
                ropeh[0][1] += y

                # check tail 1 - 9 and decide if movement required (tired, not optimized, but does the job)
                for i in range(1, n):
                    if abs(ropeh[i][0] - ropeh[i-1][0]) > 1:
                        ropeh[i][0] += 1 if (ropeh[i-1][0] - ropeh[i][0]) > 0 else - 1
                        if abs(ropeh[i][1] - ropeh[i-1][1]) > 0:
                            ropeh[i][1] += 1 if (ropeh[i-1][1] - ropeh[i][1]) > 0 else - 1

                    elif abs(ropeh[i][1] - ropeh[i-1][1]) > 1:
                        ropeh[i][1] += 1 if (ropeh[i - 1][1] - ropeh[i][1]) > 0 else - 1
                        if abs(ropeh[i][0] - ropeh[i-1][0]) > 0:
                            ropeh[i][0] += 1 if (ropeh[i-1][0] - ropeh[i][0]) > 0 else - 1

                    if i == p1:
                        touched1.add((ropeh[i][0],ropeh[i][1]))
                    elif i == p2:
                        touched2.add((ropeh[i][0], ropeh[i][1]))

                #print(f"line: {line}, head:{ropeh[0]}, tail:{ropeh[1]}, tail1:{ropeh[2]}, tail2:{ropeh[3]}, tail3:{ropeh[4]}, tail4:{ropeh[5]}, tail5:{ropeh[6]}, tail6:{ropeh[7]}, tail7:{ropeh[8]}")

    print(f"Day9 Part 1:{len(set(touched1))}")
    print(f"Day9 Part 2:{len(set(touched2))}")
