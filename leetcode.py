class Solution:
    '''
    Problem: https://leetcode.com/problems/contains-duplicate/
    '''
    def containsDuplicate(self, nums: list[int]) -> bool:
        numsSet = set()
        '''
        The "in" keyword has 2 uses in python
        1. To iterate over a collection in a for loop
        2. To check if a value is present in a collection
        '''
        for currentNum in nums:
            if currentNum in numsSet: return True
            numsSet.add(currentNum)
        return False

    '''
    Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    '''
    def maxProfit(self, prices: list[int]) -> int:
        maxSum = 0
        lowerNum = prices[0]
        '''
        We need to track the lower number and the max difference until i,
        update the max  when needed and the lower number too.
        Whenever a lower number is found we already found the max difference for the previous lower number
        and any differences starting from that point will always be greater with the new lower number,
        so we're free to update the lower number to the new one 
        '''
        for i in range(1, len(prices)):
            currentNum = prices[i]
            if(currentNum - lowerNum > maxSum): maxSum = currentNum - lowerNum
            elif (currentNum < lowerNum): lowerNum = currentNum
        return maxSum
    
    '''
    Problem: https://leetcode.com/problems/two-sum/
    '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numToIndex = {}
        '''
        Using a dictionary to hold previously visited numbers and their index is very good
        to lookup for the difference between the target value and the current value getting in the for loop
        that way whenever we already found the difference in the dictionary the function will return immediately
        '''
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []
    

resolution = Solution()
print(resolution.maxProfit([7,1,5,3,6,4]))
print(resolution.twoSum([4,2,6,9,2], 11))
print(resolution.containsDuplicate([1,2,35,1,7]))