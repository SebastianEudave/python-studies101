class Solution:
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