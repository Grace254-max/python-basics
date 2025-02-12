#open(filename,mode)
#r-read,m-write,a-append
#WRITE TO A FILE
x=open("demo.txt","w")
x.write("this is python")
x.close()\
#APPEND
x=open("demo.txt","a")
x.write("this is a new line appended \n")
x.close()
#read
x=open("demo.txt","r")
print(x.read())
x.close()