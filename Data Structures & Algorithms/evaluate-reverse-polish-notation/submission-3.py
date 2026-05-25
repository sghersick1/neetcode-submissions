class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for token in tokens:
            if token == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                res = n1 + n2
                stack.append(res)
            elif token == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                res = n2 - n1 
                stack.append(res)
            elif token == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                res = n1 * n2
                stack.append(res)
            elif token == "/": 
                n1 = stack.pop()
                n2 = stack.pop()
                res = int(float(n2)/n1)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()   
