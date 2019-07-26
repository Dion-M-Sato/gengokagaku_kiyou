import fileinput

for line in fileinput.input("2nd.md", inplace=True):
    print "%d: %s" % (fileinput.filelineno(), line),
