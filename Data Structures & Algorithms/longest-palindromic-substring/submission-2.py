class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the inclusive left and right bounds, and the length
            return [right - 1, left + 1, right - left - 1]

        ans_right, ans_left = 0, 0

        for i in range(len(s)):
            one_letter = expandAroundCenter(i, i)
            two_letter = expandAroundCenter(i, i + 1)

            if one_letter[2] > (ans_right - ans_left):
                ans_right = one_letter[0]
                ans_left = one_letter[1]
            if two_letter[2] > (ans_right - ans_left):
                ans_right = two_letter[0]
                ans_left = two_letter[1]

        # No need for +1 here; right bound is already inclusive in your logic
        return s[ans_left: ans_right + 1]
