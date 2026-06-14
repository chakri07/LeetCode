class Solution:
    def search(self, nums: List[int], t: int) -> int:
        left,right = 0, len(nums)-1

        while left <= right: 
            mid = (left+ right)//2
            
            if nums[mid] == t: 
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= t < nums[mid]:
                    right = mid - 1
                else :
                    left = mid + 1
                
            else:
                if nums[mid] < t <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1 
        
        return -1
