class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pivot = self.getPivot(nums)
        print(pivot)
        if target == nums[0]:
            return 0
        elif target > nums[0]:
            return self.binarySearch(nums[0:pivot+1],target)
        else:
            a = self.binarySearch(nums[pivot+1:],target)
            print(a)
            if a == -1 :
                return -1
            else:
                return pivot + a +1

        
    def binarySearch(self,nums: list[int], target: int) -> int:
        print(nums)
        if( len(nums) ==0 ):
            return -1
        if len(nums)==1 :
            if nums[0] == target:
                return 0
            else :
                return -1
        else:
            left = 0 
            right = len(nums) -1
            while(left < right):
                mid = (left + right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1 
                else :
                    right = mid
        return -1

    def getPivot(self,nums: list[int]) -> int:
        left = 0 
        right = len(nums) -1 
        while(left<right):
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid +1
                if nums[mid] > nums[mid+1]:
                    return mid  
            else:
                right = mid 
            


def main():
    obj = Solution()
    print(obj.search([4,5,6,7,0,1,2],7))
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
            
            
            