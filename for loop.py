#for loop-for iterating through lists,tuples strings
#loop in a string
for x in "hello":
    print(x)
    #loop in a list
    users=["alice","mary" ,"jane", "john","peter"]
    for y in users:
        print(y)
        #loop through a range
        for z in range(5):
            print(z)
fruits=["apple","mango","banana","pineapple"]
for a in fruits:
    if a=="banana":
        break
    print(a)

    if a=="banana":
        continue
