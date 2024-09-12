list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = []
""" for i in range(len(list1)):
    if list1[i] != "":
        list2.append(list1[i]) """

""" for i in list1:
    if i != "":
        list2.append(i) """

res = list(filter(None, list1))
print(res)
