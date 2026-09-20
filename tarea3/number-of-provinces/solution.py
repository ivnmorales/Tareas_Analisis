class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visitado = [False] * n

        def dfs(ciudad):
            visitado[ciudad] = True

            for vecino in range(n):
                if isConnected[ciudad][vecino] == 1 and not visitado[vecino]:
                    dfs(vecino)

        provincias = 0

        for ciudad in range(n):
            if not visitado[ciudad]:
                provincias += 1
                dfs(ciudad)

        return provincias