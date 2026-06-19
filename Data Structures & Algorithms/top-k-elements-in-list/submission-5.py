class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0 
            
            freq_map[num] += 1
        
        # intialize with empty array for max size of array
        buckets = [[] for _ in range(len(nums)+1)]
        
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        ans = []
        for i in range(len(nums),-1,-1):
            bucket = buckets[i]
            for num in bucket:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        return []


