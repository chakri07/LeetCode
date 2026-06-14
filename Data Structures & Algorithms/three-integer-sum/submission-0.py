class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i in range(len(nums)-2) :
            left = i + 1
            right = len(nums)-1
            while left < right : 
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0 :
                    solution = sorted([nums[i],nums[left],nums[right]])
                    if solution not in ans : 
                        ans.append(solution)
                    left = left + 1
                elif sum < 0 : 
                    left = left + 1
                elif sum > 0 : 
                    right = right - 1


        return ans
