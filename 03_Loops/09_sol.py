# check if all the elements are unique in a list
list =["apple","banana","orange","orange","apple","mango"]

unique_item = set()
for item in list :
    if item in unique_item:
        print("Duplicate : ",item)
        break
    unique_item.add(item)
