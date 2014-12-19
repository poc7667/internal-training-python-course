
names ={
    "good_guys":["danny"],
    "bad_guys":["poc","ethan","victor"]   
}

for key, value in names.iteritems():
    print '\n'
    print "key: "+ key
    print "value: {0} length: {1}".format(value, len(value))
