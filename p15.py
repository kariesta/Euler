'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

'''
const int gridSize = 20;
long[,] grid = new long[gridSize+1, gridSize+1];

//Initialise the grid with boundary conditions
for (int i = 0; i < gridSize; i++) {
    grid[i, gridSize] = 1; grid[gridSize,i] = 1;
}

for (int i = gridSize - 1; i >= 0; i--) {
    for (int j = gridSize - 1; j >= 0; j--) {
        grid[i, j] = grid[i+1, j] + grid[i, j+1];
    }
}
'''
s = 20
row = [[0]*(s+1)]*(s+1)
#print(row)
for i in range(s):
    row[i][s] = 1
    row[s][i] = 1

for i in range(s-1,0,-1):
    for j in range(s-1,0,-1):
        row[i][j] = row[i+1][j] + row[i][j+1]
        for r in row:
            print(r)

'''
const int gridSize = 20;
long paths = 1;

for (int i = 0; i < gridSize; i++) {
    paths *= (2 * gridSize) - i;
    paths /= i + 1;
}
'''
paths =1
for i in range(s):
    paths*=(2*s)-i
    paths/=i+1
    print(paths)


s = 21 #sides
row = [0]*s

for n in range(s):
    for r in row:
        print("h",r)
    row[0] = 1
    for m in range(1,(s)):
        row[m] += row[m-1]
    print("lolo")
    print(row)
    print("lele")
    print("\n",["{:11.0f}".format(g) for g in row])
print("row")
#below is double up
rs = row
while len(rs) > 1:
    result = []
    for r in range(1,len(rs)):
        result.append(rs[r-1]+rs[r])
    rs = result
    print(rs)
#"print("{:11.0f}".format(nsum[m]*10**(50-m)),"\t",nsum[m])

print(["{:11.0f}".format(r**2) for r in row])
#35345263800
#137846528820
