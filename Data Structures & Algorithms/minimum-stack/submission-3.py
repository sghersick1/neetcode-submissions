import math

class MinStack:

    def __init__(self):
       self.stack = []

    def push(self, val: int) -> None:
       self.stack.append(val) 

    def pop(self) -> None:
       self.stack.pop() 

    def top(self) -> int:
       return self.stack[-1]

    def getMin(self) -> int:
        min_el = math.inf
        for el in self.stack:
            min_el = min(min_el, el)
        return min_el