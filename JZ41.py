import heapq


class Solution:
    def __init__(self):
        self.maxHeap = list()
        self.minHeap = list()
        self.count = 0

    def Insert(self, num: int):
        maxLen = len(self.maxHeap)
        minLen = len(self.minHeap)
        if maxLen == 0:
            heapq.heappush(self.maxHeap, (-num, self.count, num))
        elif maxLen == minLen:
            if num >= self.maxHeap[0][-1]:
                heapq.heappush(self.minHeap, (num, self.count, num))
            else:
                heapq.heappush(self.maxHeap, (-num, self.count, num))
        elif maxLen > minLen:
            heapq.heappush(self.maxHeap, (-num, self.count, num))
            _, c, n = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, (n, c, n))
        else:
            heapq.heappush(self.minHeap, (num, self.count, num))
            _, c, n = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, (-n, c, n))
        self.count += 1

    def GetMedian(self) -> float:
        maxLen = len(self.maxHeap)
        minLen = len(self.minHeap)
        if maxLen == minLen:
            l = self.maxHeap[0][-1]
            r = self.minHeap[0][-1]
            return (l + r) / 2
        elif maxLen > minLen:
            return self.maxHeap[0][-1]
        else:
            return self.minHeap[0][-1]
