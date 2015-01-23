#!/usr/local/bin/python
import fnmatch
import os
import uniout

matches = []
for root, dirnames, filenames in os.walk('walk_this_dir'):
    print("root : {0}".format(root))
    print("dirnames : {0}".format(dirnames))
    print("filenames : {0}".format(filenames))
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))

print matches
