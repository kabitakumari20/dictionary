# datas= [{"name":"komal","score":40, "school":"pyds"},{"name":"koma","score":40,
# "school":"pyd"},{"name":"jaya","score":60,"school":"pyds"},{"name":"Sonam","score":60,
# "school":"Union"},{"name":"Akshit","score":50,"school":"Summer Fileld school"}]
# this is data in json formate so first u need to convert into dict and after that I want data all match is pyds school or and student should be score is grater than 50

datas= [{"name":"komal","score":40,"school":"pyds"},{"name":"koma","score":40,"school":"pyd"},{"name":"jaya","score":60,"school":"pyds"},{"name":"Sonam","score":60,"school":"Union"},{"name":"Akshit","score":50,"school":"Summer Fileld school"}]
# for index in range(0,len(datas)):
index=0
while index<len(datas):
    for key  in datas[index]:
        if datas[index]["score"]>50:
            if datas[index]["school"]=="pyds":
                print(datas[index])
                break
    index=index+1
