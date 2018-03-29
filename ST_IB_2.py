import numpy as np
from scipy import spatial

#------------------------------------------------
#read population file
popArr = np.loadtxt('popdata.txt',delimiter=',') 
#------------------------------------------------
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

# numPts = 10
#------------------------------------------------
#------------------------------------------------
# create/read grid points
# grdArr =
#------------------------------------------------


#build k/d tree index on cases
sTree = spatial.cKDTree(inXYT_s[:,:2])

#initialize variables
stNeighIndex = []    #stores indexes of spatiotemporal neighbors

mNN = np.inf        #minimum number of neighbors
NN = 10            #number of nearest neighbors to search for
i = 65              # iterator variable

#loop through all data points
# while i < numPts:
while i < 200:

    #query point
    sCoord = inXYT_s[i,:2]
    tCoord = inXYT_s[i,2]

    #query the tree, input number of neighbors
    sNeigh = sTree.query(sCoord,3000)
    tNeigh = []
    current = 0
    while inXYT_s[current,2] < inXYT_s[i,2]:
        tNeigh.append(current)
        current += 1

    #intersect spatial and temporal neighbors
    stNeigh = np.intersect1d(list(sNeigh[1]), tNeigh)  #indices
    # stNeighIndex.append(list(stNeigh))
    # print(list(stNeigh))

    #keep track of minimum number of spatiotemporal neighbors
    nSTN = stNeigh.size #number of space-time neighbors
    if nSTN < mNN:
        mNN = nSTN
    print(i, nSTN)

    i += 1

print(mNN)
##
#####initiate variables
####j = 0
####
#####loop through neighSIndex
####while j < numPts:
####
####    #kth space-time neighbor index
####    kNNIndex = neighSTIndex[j][mNN-1]
####
####    bwS = neighSIndexdict[j].get(neighSTIndex[j][mNN-1])
####
####    print(neighSTIndex[j][mNN-1], bwS)
######    bwT
####
######    bwS = neighSTIndex[j][mNN-1]
######    print(neighS[0][bwS])
######    print(neighT[0][bwS])
####
####    # for k in bwS:
####    #     # print(inXY[int(k)], )
####    #     print(neighS[1][mNN])
####
####    j += 1
##
