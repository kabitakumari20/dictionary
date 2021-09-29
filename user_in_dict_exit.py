# 2. Write a Python script to add a key to a dictionary. Go to the editor

# num = {0: 10, 1: 20}
# num[2]=30
# print(num)
# anothre wey
# num = {0: 10, 1: 20}
# num[2]=30
# num.update({3:30})
# print(num)

dict={"name":"raju","marks":56}
user=input("enter the user=")
if user in dict:
    print("exits")
else:
    print("not exits")