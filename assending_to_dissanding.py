# assinding to dissing print lrwaye


my_dict={"a":90, "b":78, "c":12,"d":45,"e":24}
i=0
store=0
while i<len(my_dict):
    j=0
    while j<len(my_dict):
        if my_dict[i] < my_dict[j]:
            store=my_dict[i]
            my_dict[i]==my_dict[j]
            my_dict[i]==store
        j=j+1
    i=i+1
print(my_dict)
# for key in my_dict:
    