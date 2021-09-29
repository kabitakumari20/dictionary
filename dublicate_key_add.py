d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
d={}
for i in d1:
    for j in d2:
        if i==j:
            d[i]=d1[i]+d2[j]
            break
    else:
        d[i]=d1[i]
        d[j]=d2[j]
print(d) 