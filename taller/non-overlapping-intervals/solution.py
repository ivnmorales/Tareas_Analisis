class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        quedan = 0
        fin_anterior = float('-inf')

        for inicio, fin in intervals:
            if inicio >= fin_anterior:  
                quedan += 1
                fin_anterior = fin
        return len(intervals) - quedan   
