class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            if num in freq_map: 
                freq_map[num] +=1
            else:
                freq_map[num] = 1

        # now sort the frequ_map 

        sorted_freq_map = dict(sorted(freq_map.items(),
            key = lambda item: item[1],
            reverse = True))

        print(sorted_freq_map)

        return list(sorted_freq_map.keys())[:k]
        