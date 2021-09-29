# a_dictionary = {"a": 1, "b": 2, "c": 3}
# max_key = max(a_dictionary, key=a_dictionary.get)
# print(max_key)


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
for key in (d2):
    if key in d1:
        d2[key]=d2[key]+d1[key]
d3={**d1,**d2}
print(d3)
