class TimeMap:

    def __init__(self):
        self.map = {} 
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[(key, timestamp)] = value

        if key not in self.time_map:
            self.time_map[key] = [timestamp] 
        else:
            self.time_map[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        stamps = self.time_map[key]
        recent = -1
        for stamp in stamps:
            if stamp <= timestamp:
                recent = max(recent, stamp)

        return "" if recent == -1 else self.map[(key, recent)]