class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visti = {}  # Mappa: valore -> indice
        
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in visti:
                return [visti[complemento], i]
            visti[num] = i
            
        return []