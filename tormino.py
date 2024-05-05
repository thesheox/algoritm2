# Python3 program to place tiles
size_of_grid = 0
b = 0
a = 0
cnt = 0
arr = [[0 for i in range(128)] for j in range(128)]


def place(x1, y1, x2, y2, x3, y3):
    global cnt
    cnt += 1
    arr[x1][y1] = cnt;
    arr[x2][y2] = cnt;
    arr[x3][y3] = cnt;


def tile(n, x, y):
    global cnt
    r = 0
    c = 0
    if (n == 2):
        cnt += 1
        for i in range(n):
            for j in range(n):
                if (arr[x + i][y + j] == 0):
                    arr[x + i][y + j] = cnt
        return 0;
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (arr[i][j] != 0):
                r = i
                c = j


    if (r < x + n / 2 and c < y + n / 2):
        place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2))

    elif (r < x + int(n / 2) and c >= y + int(n / 2)):
        place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1,
              y + int(n / 2) - 1)

    elif (r >= x + int(n / 2) and c < y + int(n / 2)):
        place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1,
              y + int(n / 2) - 1)

    elif (r >= x + int(n / 2) and c >= y + int(n / 2)):
        place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2) - 1,
              y + int(n / 2) - 1)

    tile(int(n / 2), x, y);
    tile(int(n / 2), x, y + int(n / 2));
    tile(int(n / 2), x + int(n / 2), y);
    tile(int(n / 2), x + int(n / 2), y + int(n / 2));

    return 0


size_of_grid = 4
a = 2
b = 0
arr[a][b] = "*"
tile(size_of_grid, 0, 0)

n=size_of_grid
size=((n*n)-1)//3
result=[[] for x in range(size)]
counter=0
for i in range(size_of_grid):
    for j in range(size_of_grid):
        counter+=1
        for k in range(size+1):
            if arr[i][j]==k:
                result[k-1].append(counter)

        print(arr[i][j], end=" ")
    print()


for i in range(len(result)):
    print("t"+str(i+1)+": "+str(result[i]))
# print(result)
