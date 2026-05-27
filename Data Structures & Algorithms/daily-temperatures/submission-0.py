class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force
        result = []
        for i, temp in enumerate(temperatures):
            day_ctr = 0
            for j in range(i+1, len(temperatures)):
                day_ctr += 1
                if temperatures[j] > temp:
                    break;
                
                if j == len(temperatures) - 1:
                    day_ctr = 0
            
            result.append(day_ctr)

        return result