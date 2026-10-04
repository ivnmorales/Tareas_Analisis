class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       
        intervals.sort(key=lambda x: x[0])
        resultado = [intervals[0]]

        for inicio, fin in intervals[1:]:
            ultimo = resultado[-1]
            if inicio <= ultimo[1]:         
                ultimo[1] = max(ultimo[1], fin)
            else:                          
                resultado.append([inicio, fin])
        return resultado
