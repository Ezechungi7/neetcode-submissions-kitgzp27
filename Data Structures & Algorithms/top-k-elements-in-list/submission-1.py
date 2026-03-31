class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        array_2d = [[-value, key] for key, value in d.items()]
        print(array_2d)
        heapq.heapify(array_2d)
        res = []
        for i in range(k):
            res.append(array_2d[0][1])
            array_2d = array_2d[1:]
            heapq.heapify(array_2d)
        return res
        

                