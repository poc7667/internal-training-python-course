raw_name_list = [
    "poc",
    "jimmy",
    "ethan",
    "danny",
    "jimmy",
    "carlos"
]


uniq_lst_by_looping = []
for name in raw_name_list:
    if name not in uniq_lst_by_looping:
        uniq_lst_by_looping.append(name)
        print(uniq_lst_by_looping)
    else:
        print("{0} is already in it".format(name))


print raw_name_list
print uniq_lst_by_looping