students = [
        ['bryant', 'C', 15],
        ['zebra', 'Z', 6],
        ['adam', 'B', 10],
]

print("Original list")
print(students)

for i in range(3):
    print("sorted by column: {0}".format(i))
    print sorted(students, key = lambda x : x[i])
