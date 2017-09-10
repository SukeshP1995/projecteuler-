grid = []
for grid_i in range(20):
   grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
   grid.append(grid_t)
m = 0
for x in range(20):
    for y in range(20):
        if x < 17:
            p = grid[x][y]*grid[x+1][y]*grid[x+2][y]*grid[x+3][y]
            if p > m:
                m = p
        if y < 17:
            p = grid[x][y]*grid[x][y+1]*grid[x][y+2]*grid[x][y+3]
            if p > m:
                m = p
        if x > 2 and y <17:
            p = grid[x][y]*grid[x-1][y+1]*grid[x-2][y+2]*grid[x-3][y+3]
            if p > m:
                m = p
        if x < 17 and y < 17:
            p = grid[x][y]*grid[x+1][y+1]*grid[x+2][y+2]*grid[x+3][y+3]
            if p > m:
                m = p
print(m)