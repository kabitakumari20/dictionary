dic1={1:23,2:45}
dic2={3:56,4:89}
dic3={5:78,6:90}
list1=[dic1,dic2,dic3]
dic4={}
i=0
while i<len(list1):
    j=0
    for j in list1[i]:
        dic4[j]=list1[i][j]
    i=i+1
print(dic4)