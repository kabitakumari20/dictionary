# Ek code likhiye jo dictionary ki 3 highest value print karaye. Example :-
# from heapq import nlargest
my_dict = {'a':50, 'b':58, 'c': 56,'d':40, 'e':100, 'f': 20}  
list=[]
max1=0
max2=0
max3=0
for key in my_dict:
    for value in my_dict:
        if my_dict[key]>max1:
            max1=my_dict[key]
        elif max1>my_dict[value] and max2<my_dict[value]:
            max2=my_dict[value]
        elif max2>my_dict[value] and max3<my_dict[value]:
            max3=my_dict[value]
list.append(max1)
list.append(max2)
list.append(max3)
print(list)

