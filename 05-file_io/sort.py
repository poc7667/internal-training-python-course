import pprint
people =  [
    ["Apple", 500, 1000],
    ["Zebra", 5000,500],
    ["Carlos", 5, 3]
]
print sorted(people, key = lambda x : x[-1])
print sorted(people)