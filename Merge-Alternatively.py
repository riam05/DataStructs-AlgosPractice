class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        merged_str = ""
        i = 0

        while i < length1 and i < length2:
            merged_str += word1[i] + word2[i]
            i += 1
        
        if length1 > length2:
            merged_str += word1[length2:]
        else:
            merged_str += word2[length1:]
        
        return merged_str