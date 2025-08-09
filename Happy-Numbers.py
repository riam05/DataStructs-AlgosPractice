class Solution:
    def getSquareSum(self, n):
        sum_squares = 0
        while(n > 0):
            print(n>0)
            modulus = n%10
            sum_squares += modulus*modulus
            n = n//10
        return sum_squares

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = 0
        fast = self.getSquareSum(n)
        while slow != fast and slow != 1 and fast != 1:
            slow = self.getSquareSum(slow)
            fast = self.getSquareSum(self.getSquareSum(fast))
        return slow == 1 or fast == 1