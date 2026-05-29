class TimeMap:

    def __init__(self):
        self.map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(value, timestamp)]
        else:
            self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        values = self.map[key]

        l, r = 0, len(values) - 1
        result = ""
        while l <= r and values[l][1] <= timestamp: 
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                result = values[m][0] # Value
                l = m + 1
            else:
                r = m - 1

        return result 
        