class Solution:
    def jump(self, nums: List[int]) -> int:
        nums[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                nums[i] = -1
                continue
            min_so_far = len(nums)
            if nums[i] >= len(nums) - 1 - i:
                nums[i] = 1
                continue
            for j in range(i + nums[i], i, -1):
                if nums[j] >= 0 and nums[j] < min_so_far:
                    # print(j, nums[j], nums)
                    min_so_far = nums[j] + 1
            nums[i] = min_so_far
            
        return nums[0]