with open("example.txt","w")as y:
    y.write("hello goodafternoon \n")
    y.write("this is python \n")
#append
with open("example.txt","a")as y:
    y.write("new line appended")
#read
with open("example.txt","r")as x:
    print(x.read())