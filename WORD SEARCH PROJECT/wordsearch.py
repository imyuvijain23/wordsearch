from random import randint as r
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
WORDS = ["AMITGHOSH", "KATIE", "KEVIN", "MEHUL"]
DIM = 10

X = []

def add(c, word, reverse=False, vertical=False, diagonal=False):
    letters = list(word)
    x,y = c[0], c[1]
    if reverse:
        letters = letters[::-1]

    if len(word) > DIM:
        return ValueError
    for COUNT in range(len(letters)):
        if vertical:
            X[x+COUNT][y] = letters[COUNT]
        elif diagonal:
            X[x+COUNT][y+COUNT] = letters[COUNT]
        else:
            X[x][y+COUNT] = letters[COUNT]
        COUNT += 1

def output():
    i = 0
    print("  ", end="")
    for j in range(DIM):
        if j < 10:
            print(f"0{j}", end=" ")
        else:
            print(j, end=" ")
    print()
    for x in X:
        if i < 10:
            print(f"0{i}", end="|")
        else:
            print(i, end="|")
        for y in x:
            # if y == "-":
            #     y = alpha[r(0,25)]
            print(y, end="  ")
        print()
        i += 1



def coord(word, vertical=False, diagonal=False):
    L = len(word)
    
    while True:
        x, y = r(0, DIM - L), r(0, DIM - L)
        
        check = len(word)

        for COUNT in range(L):
            if vertical:
                if X[x + COUNT][y] != "-":
                    break
                else:
                    check -= 1
            elif diagonal:
                if X[x + COUNT][y + COUNT] != "-":
                    break
                else:
                   check -= 1
            else:
                if X[x][y + COUNT] != "-":
                    break
                else:
                    check -= 1
        if check == 0:
            break
    return x,y

def create():
    global X
    X = []
    for i in range(DIM):
        X.append(list("-"*DIM))

    for i in WORDS:
        ver = dia = False

        orientation = r(0,2) #horizontal, diagonal, vertical 
        
        if orientation == 1:
            dia = True
        elif orientation == 2:
            ver = True

        rev = [True, False][r(0,1)] #reverse
        c = coord(i, vertical=ver)
        add(c, i, vertical=ver, reverse=rev, diagonal=dia)
        print(c, i)

#OUTPUT
# output()
def ws():
    create()
    NEW = X[:]
    rows = len(NEW)
    for i in range(rows):
        chs = len(NEW[i])
        for ch in range(chs):
            if NEW[i][ch] == "-":
                NEW[i][ch] = alpha[r(0,25)]

    return NEW, WORDS

output()