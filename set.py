#sets are unordered,unchangeable and do not allow duplicates
myclasses={"chrome", "safari","firefox","mozilla"}
print(myclasses)
print(type(myclasses))
print(myclasses)
#loop
for x in myclasses:
    print(x)
    #set()constructor
    myclasses.add("brave")
    print(myclasses)
    #set()constructor