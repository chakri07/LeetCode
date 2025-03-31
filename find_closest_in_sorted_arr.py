
from typing import List


class Solution:
    def findClosest(self, arr, k):
        if len(arr) == 0:
            return None
            
        if k <= arr[0]:
            return arr[0]
        
        if k >= arr[-1]:
            return arr[-1]
        
        left = 0 
        right = len(arr)-1 
        closest = arr[0]
        diff = abs(closest-k)
        
        while left <= right:
            mid = left+right // 2
            
            if arr[mid] == target:
                return arr[mid]
            else:
                if diff < abs(arr[mid]-k):
                    diff = abs(arr[mid]-k)
                    closest = arr[mid]
                elif diff == abs(arr[mid]-k):
                    closest = max(arr[mid],closest)
            
            if arr[mid] < k:
                left = mid + 1
            elif arr[mid] > k:
                right = mid -1 
                
        return closest

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findClosest(A, D)
        print(ans)
        print("~")

# } Driver Code Ends


