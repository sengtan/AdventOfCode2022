import re

dirsize = {}

class folder:
    def __init__(self, name, parent, children):
        self.name = name
        self.parent = parent
        self.path = f"{self.parent.path}/{self.name}" if parent else name
        self.children = children

    def goInto(self, name):
        return [x for x in self.children if x.name == name][0]

    def goOut(self):
        return self.parent

    def getSize(self):
        global dirsize
        if self.children:
            size = 0
            for child in self.children:
                size += child.getSize()
            dirsize[self.path] = size
            return size
        else:
            dirsize[self.path] = 0
            return 0

    def __str__(self):
        str = f"[name:{self.name} children:{[x.name for x in self.children]}]"
        return str

class file:
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.path = f"{self.parent.path}/{self.name}" if parent else name
        self.size = size

    def getSize(self):
        return self.size

if __name__ == "__main__":
    home = folder("/",None,[])
    cursor = home
    listing = False

    #change directory
    cd = re.compile(r"\$ cd (\S+)",re.IGNORECASE)

    #directories
    dir = re.compile(r"dir (\S+)",re.IGNORECASE)

    #files
    fil = re.compile(r"(\d+) (\S+)",re.IGNORECASE)

    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            # if changing directory, means listing ended
            mat = cd.findall(line)
            if mat:
                mat = mat[0]
                if mat == "/":
                    cursor = home
                elif mat == "..":
                    cursor = cursor.goOut()
                else:
                    cursor = cursor.goInto(mat)
                listing = False
                continue

            # if it is listing, and it is either directory/file
            if listing:
                mat = dir.findall(line)
                if mat:
                    mat = mat[0]
                    cursor.children.append(folder(mat,cursor,[]))
                    continue
                mat = fil.findall(line)
                if mat:
                    mat = mat[0]
                    cursor.children.append(file(mat[1],cursor,int(mat[0])))
                    continue

            #if list, continue next line
            if line == "$ ls":
                listing = True
                continue

    #once mapped out all directories/files, ask all nodes/dir to report their size, starting from home directory
    home.getSize()

    # part 1
    total = 0
    required = 70000000
    minimum = 30000000
    tofree = minimum - (required - home.getSize())
    suitable = []
    for k, v in dirsize.items():
        # part 1
        if v <= 100000:
            total += v

        # part 2
        if v >= tofree:
            suitable.append(v)

    print(f"Day7 Part 1:{total}")
    print(f"Day7 Part 2:{min(suitable)}")
