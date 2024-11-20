from wordsearch import ws, DIM, output

X = ws()

output()
print("+++++\n\n\n\n\n")

def search(word):
    
    for x in range(DIM):
        for y in range(DIM):

            if X[x][y] == word[0]:
                neword = word[0]
                dir = -1 #0, 1, 2, 3, 4, 5, 6, 7
                LAST = 0
                for c in range(1, len(word)):

                    if x+c < DIM-1:

                        if X[x+c][y] == word[c] and (dir == 0 or dir==-1):
                            dir = 0
                            neword += (X[x+c][y])
                        
                        if X[x+c][y-c] == word[c] and (dir == 6 or dir==-1):
                            neword += (X[x+c][y-c])

                    if y+c < DIM-1:
                        if X[x-c][y+c] == word[c] and (dir == 7 or dir==-1):
                            neword += (X[x-c][y+c])

                        
                            
                        if X[x][y+c] == word[c] and (dir == 2 or dir==-1):
                            dir = 2
                            neword += (X[x][y+c])

                    if y+c  < DIM-1 and x+c < DIM-1:
                        if X[x+c][y+c] == word[c] and (dir == 1 or dir==-1):
                            dir = 1
                            neword += (X[x+c][y+c])

                    if X[x-c][y] == word[c] and (dir == 3 or dir==-1):
                        dir = 3
                        neword += (X[x-c][y])

                    if X[x-c][y-c] == word[c] and (dir == 4 or dir==-1):
                        dir = 4
                        neword += (X[x-c][y-c])
                        
                    if X[x][y-c] == word[c] and (dir == 5 or dir==-1):
                        neword += (X[x][y-c])
                    if c == len(word)-1:
                        LAST = c
                if neword == word:
                    print("WORD FOUND at", x, y, "to", )
                    break


search("MEHUL")