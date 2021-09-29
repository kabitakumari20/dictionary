# Write a Python program to iterate over dictionaries using for loops. Go to the editor

# nums={1:"one",2:"two",3:"three",4:"four"}
# for key in nums:
#     print(key)

list1=["one","two","three","four"]
list2=[1,2,3,4]
i=0
c={}
while i<len(list1):
    c[list1[i]]=list2[i]
    i=i+1
print(c)