class Solution:

    '''
    Problem: https://leetcode.com/problems/valid-parentheses/
    '''
    def isValid(self, s: str) -> bool:
        bracketsDict = {
            '{':'}', 
            '[': ']',
            '(': ')'
            }
        
        strStack = []

        '''
        In keyword can be used directly in dictionaries to know if a key is present.
        If the character is opening a bracket then we add it to the stack, 
        if not we need to check if it is actually closing the previous bracket
        '''
        for c in s:
            if c in bracketsDict: strStack.append(c)
            elif len(strStack) == 0 or bracketsDict[strStack.pop()] != c: 
                return False

        if len(strStack) != 0: return False
        return True

    '''
    Problem: https://leetcode.com/problems/valid-anagram/
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        '''
        Use a dictionary to store the letters that already appeared at the string
        and their frequency, then we can update the map to see if the letters are present on the map and decrease their count.
        Other solutions include arrays to increase/decrease appearance of each letter, ex. JAVA: alphabet[s.charAt(i) - 'a']++
        '''
        characterAppearance = {}
        for letter in s:
            apparencesInDict = characterAppearance.get(letter)
            if(apparencesInDict is None):
                characterAppearance[letter] = 1
            else:
                characterAppearance[letter] = apparencesInDict + 1
        for letter in t:
            apparencesInDict = characterAppearance.get(letter)
            if(apparencesInDict is None):
                return False
            elif apparencesInDict == 1:
                characterAppearance.pop(letter)
            else:
                characterAppearance[letter] = apparencesInDict - 1

        if len(characterAppearance) == 0: 
            return True
        return False

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
print(resolution.isAnagram(s = "car", t = "rat"))
print(resolution.isValid("[]{()}"))