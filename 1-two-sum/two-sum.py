class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            i_value = nums[i]
            for j in range(i+1,len(nums)):
                j_value = nums[j]
                if i_value+j_value == target:
                    output.append(j)
                    output.append(i)
                    return output
