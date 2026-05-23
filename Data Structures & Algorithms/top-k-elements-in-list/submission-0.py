class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)
        for i in nums:
            dict[i]+=1

        freqs = [[] for _ in range(len(nums)+1)]
        for num, count in dict.items():
            freqs[count].append(num)

        result=[]
        for i in range(len(freqs)-1, 0, -1):
            for num in freqs[i]:
                result.append(num)
                if len(result)==k:
                    return result

        return result

        
        
        