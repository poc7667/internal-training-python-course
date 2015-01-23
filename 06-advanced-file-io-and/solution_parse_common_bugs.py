target_line = None
fixed_bugs = []

# open file and read lines
with open("./history.txt", 'r') as f :
    for line in f :
        if "Verify major bug fixed" in line:
            target_line = line
            break
print(target_line)
