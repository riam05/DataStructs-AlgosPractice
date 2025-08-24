class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cons_count = 1
        cons_grps = []

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cons_count += 1
            else:
                cons_grps.append(cons_count)
                cons_count = 1
        cons_grps.append(cons_count)
        
        num_substrings = 0
        for i in range(1, len(cons_grps)):
            num_substrings += min(cons_grps[i], cons_grps[i-1])
        
        return num_substrings