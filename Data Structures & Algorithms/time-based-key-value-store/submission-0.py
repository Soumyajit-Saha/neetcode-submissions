class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp, value))
        else:
            self.dic[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        else:
            l = 0
            r = len(self.dic[key]) - 1
            res = ""
            while l <= r:
                mid = l + (r - l) // 2
                if self.dic[key][mid][0] == timestamp:
                    res = self.dic[key][mid][1]
                    break

                elif self.dic[key][mid][0] > timestamp:
                    r = mid - 1

                else:
                    l = mid + 1
                    res = self.dic[key][mid][1]
            
            return res
        
