# def add_dictionary(s,a):
#     sum={**s,**a}
#     return sum
    
# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# dict3=add_dictionary(s,a)
# print(dict3)

s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
c={}
for i in (s,a):
    c.update(i)
print(c) 