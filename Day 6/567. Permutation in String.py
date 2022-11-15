class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s1_count = collections.Counter(s1)
        
        for i in range(len(s2) - s1_len+1):
            s2_count = collections.Counter(s2[i:i+s1_len])
            if self.match(s1_count, s2_count):
                return True
        return False
    def match(self, s1, s2):
        if s1.keys() != s2.keys():
            return False
        for k in s1.keys():
            if s1[k] != s2[k]:
                return False
        return True