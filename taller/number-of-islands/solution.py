class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        filas = len(grid)
        columnas = len(grid[0])
        islas = 0

        for i in range(filas):
            for j in range(columnas):
                if grid[i][j] == '1':       
                    islas += 1
                    grid[i][j] = '0'        
                    pila = [(i, j)]
                    while pila:             
                        f, c = pila.pop()
                        for df, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nf, nc = f + df, c + dc
                            if 0 <= nf < filas and 0 <= nc < columnas and grid[nf][nc] == '1':
                                grid[nf][nc] = '0'
                                pila.append((nf, nc))
        return islas
