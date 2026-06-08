import bisect
class TimeMap:

    def __init__(self):
        self.keyValMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyValMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        print(self.keyValMap)
        if key not in self.keyValMap:
            return ""
        idx = bisect.bisect_right(self.keyValMap[key], [timestamp + 1]) - 1
        if idx == -1:
            return ""
        return self.keyValMap[key][idx][1]
