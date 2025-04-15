'''A tuple can be used as a key in dictionaries!'''
list = [1,2,3,4,5]
tpl = tuple(list)
result = {tpl: "1"}

print(tpl)
print(result[tpl])