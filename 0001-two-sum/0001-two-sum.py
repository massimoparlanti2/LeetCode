class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]+nums[j]==target and i!=j):
                    res.append(i)
                    res.append(j)

        return res[0:2]
