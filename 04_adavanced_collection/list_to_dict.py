raw_name_list = [
    "danny","poc","ethan","victor"
]
# names ={
#     "good_guys":["danny"],
#     "bad_guys":["poc","ethan","victor"]   
# }

names ={
    "good_guys": [123,466],
    "bad_guys": [1324,5425]
}

for name in raw_name_list:
    if name=="danny":
        names["good_guys"].append(name)
    else:
        names["bad_guys"].append(name)

print(raw_name_list)
print(names)

while True:
    search_key = raw_input(">>search for:")
    if search_key not in names:
        print("Wrong search key")
    else:
        print names[search_key]