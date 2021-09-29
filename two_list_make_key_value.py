list1=[1,2,3,4,5,6,7]
list2=[8,9,10,11,12,13,14]
c={}
i=0
while i<len(list1):
    c[list1[i]]=list2[i]
    i=i+1
print(c)