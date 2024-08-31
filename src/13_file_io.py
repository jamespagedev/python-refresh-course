"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
# YOUR CODE HERE
import os
dirname = os.path.dirname(os.path.abspath(__file__))
filenameFoo = 'foo.txt'
filenameFooWithPath = os.path.join(dirname, filenameFoo)
# --------------------------
# f = open(filenameWithPath, 'r')
# print(f.read())
# f.close()
# ----------- or -----------
# better practice, because no f.close() required
with open(filenameFooWithPath, 'r') as f:
    print(f.read())
# --------------------------

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
filenameBar = 'bar.txt'
filenameBarWithPath = os.path.join(dirname, filenameBar)
with open(filenameBarWithPath, 'w+') as f:
    for i in range(1, 4):  # lines 1-3
        f.write("This is line %d\n" % (i))
with open(filenameBarWithPath, 'a+') as f:
    for i in range(4, 7):  # lines 4-6
        f.write("This is line %d (appended)\n" % (i))