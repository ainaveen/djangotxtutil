import os
#
##Ref :https://www.guru99.com/reading-and-writing-files-in-python.html
#file_object  = open("filename", "mode")
f= open("sample.xml","w+")
#w+ : Read and Write
#r : Read

for i in range(10):
     f.write("This is line %d\r" % (i+1))
f.close()
# Removing/Deleting file using python
# https://www.w3schools.com/python/python_file_remove.asp
os.remove("sample.xml") 