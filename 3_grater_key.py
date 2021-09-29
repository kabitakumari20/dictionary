
# largest 3 keys
# my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# from heapq import nlargest
my_dict = {'a':50, 'b':58, 'c': 56,'d':40, 'e':100, 'f': 20}  
# three_largest = nlargest(3, my_dict,key=my_dict.get)
# print(three_largest)
list=[]
max1=0
max2=0
max3=0
for key in my_dict:
    for value in my_dict:
        if my_dict[key]>max1:
            max1=my_dict[key]
            g=key
        elif max1>my_dict[value] and max2<my_dict[value]:
            max2=my_dict[key]
            h=key
        elif max2>my_dict[value] and max3<my_dict[value]:
            max3=my_dict[key]
            i=key
list.append(g)
list.append(h)
list.append(i)
print(list)




