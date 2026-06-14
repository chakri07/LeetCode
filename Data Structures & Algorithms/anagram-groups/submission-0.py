class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_map = {}

        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in final_map: 
                final_map[sorted_s].append(s)
            else:
                final_map[sorted_s] = [s]

        return list(final_map.values())