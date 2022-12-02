if __name__ == "__main__":
    with open("input.txt") as f:
        #rock(A,X) = 1, paper(B,Y) = 2, scissors(C,Z) = 3
        #win = 6 score
        win = {'A Y':8,'B Z':9,'C X':7}

        #lose = 0 score
        lose = {'A Z':3,'B X':1,'C Y':2}

        #draw = 3 score
        draw = {'A X':4,'B Y':5,'C Z':6}

        score = {**win,**lose,**draw}

        total = 0
        smarttotal = 0

        for line in f:
            total += score[line.strip()]

            if line[2] == 'X':
                smarttotal += [v for k, v in lose.items() if line[0] in k][0]
            elif line[2] == 'Y':
                smarttotal += [v for k, v in draw.items() if line[0] in k][0]
            else:
                smarttotal += [v for k, v in win.items() if line[0] in k][0]

    print(f"Day2 Part 1:{total}")
    print(f"Day2 Part 2:{smarttotal}")