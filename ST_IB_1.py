import numpy as np
from scipy import spatial

#------------------------------------------------
# read case points file
disFile = open('AllCases2010_11_clip.txt', "r")
inXYT = []
disFile.readline()
for record in disFile:
    inXYT.append([float(record.split("\t")[0]),float(record.split("\t")[1]),float(record.split("\t")[2])])
disFile.close()
numPts = len(inXYT)

inXYT_s = np.array(sorted(inXYT, key=lambda a: a[2]))
#------------------------------------------------

#------------------------------------------------
# open output file
outFile = open("out_1.txt",'w')

#build k/d tree index on cases
sTree = spatial.cKDTree(inXYT_s[:,:2])

#initialize variables
stNeighIndex = []    #stores indexes of spatiotemporal neighbors

mNN = np.inf        #minimum number of neighbors
NN = 4              #desired number of nearest neighbors
bN = 2000           #big number
i = 0              # iterator variable

#loop through all data points
##while i < numPts:
while i < 30:

    #query point
    sCoord = inXYT_s[i,:2]
    tCoord = inXYT_s[i,2]

    #query the tree, input number of neighbors to search for
    sNeigh = sTree.query(sCoord,bN)

    
    #search for temporal neighbors
    tNeigh = []
    
    if i < bN:
        current = 0
    else:
        current = i - bN

    #if temporal coordinate of neighbor smaller than temporal coordinate of current point, append to list    
    while inXYT_s[current,2] < inXYT_s[i,2]:
        tNeigh.append(current)
        current += 1

    print("tNeigh", tNeigh)

    #keep intersecting spatial and temporal neighbor lists until desired number of ST neighbors is reached
    stNeighLen = 0
    count = 5
    iteration = 0

    if len(tNeigh) > NN:
    
        while stNeighLen < NN and iteration < 100:
            #intersect spatial and temporal neighbors
            stNeigh = np.intersect1d(list(sNeigh[1][:count]), tNeigh[:count])  #indices
            stNeighLen = len(stNeigh)
            print("stNeighLen", stNeighLen)
            count += 1
            iteration += 1
##        
##
##    #write to file
##    s = ", ".join(map(str, list(stNeigh)))
##    outFile.write(str(i) + "," + str(sCoord[0]) + "," + str(sCoord[1]) + "," + str(tCoord) + "," + s + "\n")
##
##    #keep track of minimum number of spatiotemporal neighbors
##    nSTN = stNeigh.size #number of space-time neighbors
##    if nSTN < mNN:
##        mNN = nSTN

    i += 1

outFile.close()
print(mNN)
