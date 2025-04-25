class Solution:
    '''
    Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        sLen = len(s)
        maxCount = 0
        leftPointer = 0
        rightPointer = 1

        if(sLen == 0 or sLen == 1): return sLen

        currentSub = set()
        currentSub.add(s[0])

        '''
        By using sliding window and a set we can track what values are part of the substring and what is our current substring 
        '''
        while(rightPointer != len(s)):
            newChar = s[rightPointer]
            while newChar in currentSub:
                currentSub.remove(s[leftPointer])
                leftPointer += 1
            currentSub.add(newChar)
            currentSubSize = rightPointer - leftPointer + 1
            if currentSubSize > maxCount: maxCount = currentSubSize
            rightPointer += 1

        return maxCount

    '''
    Problem: https://leetcode.com/problems/group-anagrams/
    '''
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        resultList = []
        resultMap = {}
        '''
        Great idea to sort the strings and use it as keys, 
        other possible solution is to use a touple created from the ordered frequencies of the alphabet!
        ex. Python: keyTouple = tuple(frequencies)
        '''
        for word in strs:
            currentStr = ''.join(sorted(word))

            if  not currentStr in resultMap:
                resultMap[currentStr] = []

            resultMap[currentStr].append(word)

        for values in resultMap.values():
            resultList.append(values)

        return resultList
    

resolution = Solution()
print(resolution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))