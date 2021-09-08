class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = nums.copy()
        new_nums.sort()
        largest = new_nums[len(new_nums)-1]
        smallest = new_nums[0]
        for i,value in enumerate(nums):
            if value + largest < target or value + smallest > target:
                continue
            
            next_num = target - value
            nums_copy = nums.copy()
            data = value in nums_copy
            nums_copy.remove(value)
            if next_num in nums_copy:
                if data:
                    return [i,nums_copy.index(next_num)+1]
                else:
                    return [i,nums_copy.index(next_num)]

