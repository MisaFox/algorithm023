lists=[2,7,11,15]
def twoSum(lists,target):
    dic = {}
    for i,num in enumerate(lists):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i
print(twoSum(list1,9))
