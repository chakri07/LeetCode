class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        # Create a DP table to store matching results.
        # dp[i][j] indicates whether the first i characters of s match the first j characters of p.
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]

        # Initialize the base case: empty string matches empty pattern.
        dp[0][0] = True

        # Handle the case where the pattern starts with a sequence of '*'
        for j in range(1, p_len + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Iterate through the string and pattern, filling the DP table.
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j - 1] != '*':
                    # If the current pattern character is not '*', we need a direct match
                    # or a '.' to match.
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]  # Previous characters must also match
                    else:
                        dp[i][j] = False  # No match
                else:
                    # If the current pattern character is '*', we have two options:
                    # 1. '*' matches zero occurrences of the preceding character.
                    # 2. '*' matches one or more occurrences of the preceding character.
                    dp[i][j] = dp[i][j - 2]  # Zero occurrences

                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j] # One or more occurrences

        # The result is at the bottom-right corner of the DP table.
        return dp[s_len][p_len]