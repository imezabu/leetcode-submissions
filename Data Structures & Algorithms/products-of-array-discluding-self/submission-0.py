class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        prod=1
        for i in range(len(nums)-1):
            prod*=nums[i]
            left.append(prod)
        prod=1
        for i in range(len(nums)-1, 0, -1):
            prod*=nums[i]
            right.append(prod)

        right.reverse()
        right.append(1)
        left.insert(0,1)

        res=[]
        for i in range(len(nums)):
            res.append(left[i]*right[i])

        return res