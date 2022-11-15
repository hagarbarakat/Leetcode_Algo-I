class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Window and map
        hashmap = {}
        ans = 0 
        i = 0 
        j = 0 
        while j < len(s):
            if s[j] in hashmap:
                i = max(hashmap[s[j]], i)
            ans = max(ans, j - i + 1)
            hashmap[s[j]] = j + 1
            j += 1
        return ans