sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count_dic = dict()

for item in sample_list:
    if item in count_dic:
        count_dic[item] += 1
    else:
        count_dic[item] = 1

print(count_dic)
