class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        values = self.table[key]
        res = ''
        l, r = 0, len(values)-1
        while l <= r:
            mid = (l + r)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
