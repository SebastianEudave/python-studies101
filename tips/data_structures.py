'''
A tuple can be used as a key in dictionaries!
'''
from typing import List, Optional


list = [1,2,3,4,5]
tpl = tuple(list)
result = {tpl: "1"}

print(tpl)
print(result[tpl])

'''
Lists can be manipulated to get different lists from the original with list slicing
syntax = list_name[start : end : step]
'''
list1 = [1,2,3,4,5,6]
list2 = list1[::-1]
list3 = list[1:5:2]
print(list2)
print(list3)

def checkNull(zpids:Optional[List[int]]):
    print(len(zpids) if zpids else None)

zpids = None
checkNull(zpids=zpids)


