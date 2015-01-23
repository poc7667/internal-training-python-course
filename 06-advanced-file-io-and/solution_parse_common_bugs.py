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
