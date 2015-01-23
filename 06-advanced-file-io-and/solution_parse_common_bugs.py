target_line = None
fixed_bugs = []

# open file and read lines
with open("./history.txt", 'r') as f :
    for line in f :
        if "Verify major bug fixed" in line:
            target_line = line
            break
print(target_line)


            
#stage 2
print target_line
print target_line.split("<")[-1].split(">")[0]
trimmed_bugs_info = target_line.split("<")[-1].split(">")[0].split(",")
# print trimmed_bugs_info


# stage 3 : convert bugs into a list
for bug in trimmed_bugs_info:
    if "-" in bug:
        bug_range = bug.split("-")
        fixed_bugs += list(range(int(bug_range[0]), int(bug_range[1])+1))
    else:
        fixed_bugs.append(int(bug))
