# -*- coding: UTF-8 -*-
def appendZero(lists):    
    for i, num in enumerate(lists):
        if num == 0:
            lists.append(num)
            lists.remove(num)
			
def appendZero1(lists):          
    lists.sort(key=lambda x:x==0)

def appendZero2(lists): 	
    index = 0
    for i in range(len(lists)):
        if lists[i] != 0:
            lists[i],lists[index] = lists[index],lists[i]
            index += 1
        
lists=[0,2,6,0,1]
lists1=[0,0,0,1,2,3]
lists2=[1,0,4,0,3,0]
appendZero(lists)
appendZero1(lists1)
appendZero2(lists2)
print(lists)
print(lists1)
print(lists2)