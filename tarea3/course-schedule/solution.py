from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        grafo = [[] for _ in range(numCourses)]
        grado_entrada = [0] * numCourses

        for curso, requisito in prerequisites:
            grafo[requisito].append(curso)
            grado_entrada[curso] += 1

        cola = deque()

        for curso in range(numCourses):
            if grado_entrada[curso] == 0:
                cola.append(curso)

        completados = 0

        while cola:
            curso = cola.popleft()
            completados += 1

            for siguiente in grafo[curso]:
                grado_entrada[siguiente] -= 1

                if grado_entrada[siguiente] == 0:
                    cola.append(siguiente)

        return completados == numCourses