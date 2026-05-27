class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force
        result = [0] * len(temperatures) 
        mon_stack = [] # non-increasing order
        for i, temp in enumerate(temperatures):
            while mon_stack and mon_stack[-1][0] < temp:
                el, idx = mon_stack.pop()
                result[idx] = i - idx

            # add tuple to mon_stack
            mon_stack.append((temp, i))

        return result