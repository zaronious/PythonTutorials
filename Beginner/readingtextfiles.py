# file to open and mode to open with 'r' for read, 'w' for write
file = open("file.txt", "r")
# read the file
f = file.readlines()
file.close()
# remove \n at ends of lines by splitting into an array of lines
newlist = []
for line in f:
    if line[-1] == "\n":
        newlist.append(line[:-1])
    else:
        newlist.append(line)
print(newlist)
# alternate way, much better
newlist2 = []
for line in f:
    newlist2.append(line.strip())
print(newlist2)
