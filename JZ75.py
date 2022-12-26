class Solution:
    def __init__(self):
        self.hashMap = dict()
        self.hashSet = set()
        self.count = 0

    # 返回对应char
    def FirstAppearingOnce(self) -> str:
        if len(self.hashMap) == 0:
            return "#"
        pairs = [(v, k) for k, v in self.hashMap.items()]
        pairs.sort()
        return pairs[0][1]

    def Insert(self, char: str):
        if char in self.hashSet:
            return
        if char in self.hashMap:
            self.hashMap.pop(char)
            self.hashSet.add(char)
        else:
            self.hashMap[char] = self.count
            self.count += 1
