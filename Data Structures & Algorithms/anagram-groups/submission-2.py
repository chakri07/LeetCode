class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for word in strs:
            word_map = {}
            for char in word:
                if char in word_map:
                    word_map[char] += 1
                else:
                    word_map[char] = 1
            
            encoded_str = ''
            for key in list(sorted(word_map.keys())):
                encoded_str = encoded_str + key + str(word_map[key])

            if encoded_str in ans:
                ans[encoded_str].append(word)
            else:
                ans[encoded_str] = [word]

        return list(ans.values())
