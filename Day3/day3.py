if __name__ == "__main__":

    with open("input.txt") as f:
        total = 0
        total1 = 0
        lines = 0
        buffer = []
        for line in f:
            #part 1
            line = line.strip()
            x = set(line[:int(len(line)/2)])    #convert the first half to set
            y = set(line[int(len(line)/2):])    #convert the second half to set
            z = (x&y).pop()                     #get the intersection of both set
            total += ord(z)-38 if z.isupper() else ord(z)-96    #convert to number and add up

            #part 2
            lines+=1
            buffer.append(line)
            if lines == 3:
                u = (set(buffer[0])&set(buffer[1])&set(buffer[2])).pop()
                total1 += ord(u)-38 if u.isupper() else ord(u)-96
                lines = 0
                buffer = []

    print(f"Day3 Part 1:{total}")
    print(f"Day3 Part 2:{total1}")
