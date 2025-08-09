class Solution:
    def __init__(self):
        self.trib_values = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        # cuts down time complexity O(3^n) -> O(n)
        if n in self.trib_values:
            return self.trib_values[n]

        # else
        self.trib_values[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)

        return self.trib_values[n]