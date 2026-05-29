class TimeMap:

    def __init__(self):
       self.map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        recent = -1
        for i in range(0, timestamp + 1):
            if (key, i) in self.map:
                recent = i
        return "" if recent == -1 else self.map[(key, recent)]