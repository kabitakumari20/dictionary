# char_list='MISSISSIPPI'
# a=[]
# i=0
# while i<len(char_list):
# 	j=0
# 	b=[]
# 	count=0
# 	while j<len(char_list):
# 		if char_list[i]==char_list[j]:
# 			count=count+1
# 		j=j+1
# 	b.append(char_list[i])
# 	b.append(count)
# 	if b not in a:
# 		a.append(b)
# 	i=i+1
# 	z=dict(a)
# print(z)
str1 = 'mississppi'
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict) 
