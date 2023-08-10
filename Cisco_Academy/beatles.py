# 3.4.11 LAB The basics of lists ‒ the Beatles
beatles = []

# step 1
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
print(" Please add the following members of the band to the list: Stu Sutcliffe, and Pete Best")

for i in range(2): 
    e = input(" Please add new element: ")
    beatles.append(e)
print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))