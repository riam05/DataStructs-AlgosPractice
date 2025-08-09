class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0

        # compute sum of first window of size k
        for i in range(k):
            sum += nums[i]

        # initialize maxSum with the sum of first window
        maxSum = sum

        n = len(nums)
        for i in range(n-k):
        # Add element of list joining window, and substract element leaving window
            sum -= nums[i]
            sum += nums[i+k]
            if sum > maxSum:
                maxSum = sum
        
        average = maxSum/k

        return average
