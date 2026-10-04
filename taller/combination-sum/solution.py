class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        resultado = []
        actual = []

        def backtrack(inicio, falta):
            if falta == 0:                       
                resultado.append(actual[:])
                return
            for i in range(inicio, len(candidates)):
                if candidates[i] > falta:       
                    break
                actual.append(candidates[i])    
                backtrack(i, falta - candidates[i])
                actual.pop()                    

        backtrack(0, target)
        return resultado
