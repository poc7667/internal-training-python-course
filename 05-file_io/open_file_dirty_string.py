from pprint import pprint
iod_versions = []
for line in open('history.txt'):
    if "iod version:" in line:
        iod_versions.append(line)
pprint(iod_versions)