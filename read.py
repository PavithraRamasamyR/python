fo= open("foo.txt","r+")
str= fo.read(10);
print ("Read string is:", str)
position= fo.tell();
print ("Current file position:", position)
position= fo.seek(3,0);
str=fo.read(10)
print ("Again read string is:", str)
fo.close()

existing file test1.txt
os.remove("test1.txt","test2.txt")

delete file test2.txt
import os
os.remove("text2.txt")

to create a directory test in the current directory
import os
os.mkdir("test")

changing a directory
os.chdir("/home/newdir")

give current directory
os.getcwd()

to remove current directory 
os.rmdir("/tmp/test")
