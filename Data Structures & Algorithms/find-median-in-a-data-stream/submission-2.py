class MedianFinder:

    def __init__(self):
        self.mylist = []

    def addNum(self, num: int) -> None:
        self.mylist.append(num)
        self.mylist.sort()

    def findMedian(self) -> float:
        l = len(self.mylist)
        if (l % 2) == 1:
            return self.mylist[(l-1)//2]
        else:
            return (self.mylist[l//2] + self.mylist[l//2-1])/2
        
        