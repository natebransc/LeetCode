# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        counts = []
        if len(s) == 1:
            return 1
        i = 0
        while i < len(s):
            try:
                seen.index(s[i])
                counts.append(len(seen))
                temp = s[i]
                while i > 0:
                    if s[i - 1] == temp:
                        break
                    else:
                        i -= 1
                seen = []
                seen.append(s[i])
            except:
                seen.append(s[i])
                if i == (len(s) - 1):
                    counts.append(len(seen))
            i += 1
        max = 0
        for i in counts:
            if i >= max:
                max = i

        return max

test = Solution()

print(test.lengthOfLongestSubstring("dvdf"))