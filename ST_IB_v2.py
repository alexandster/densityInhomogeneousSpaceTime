import numpy as np
from scipy import spatial

#population
popArr = np.loadtxt('popdata.txt',delimiter=',') 

#disease cases
# disArr = np.loadtxt('casdata.txt',delimiter=',')

# read input point file
disFile = open('casdata.txt', "r")
#disFile = open('AllCases2010_11_clip.txt', "r")
inXY, inT = [], []
for record in disFile:
    inXY.append([float(record.split(",")[0]),float(record.split(",")[1])])
    inT.append([float(record.split(",")[2])])
disFile.close()
# numPts = len(inXY)
numPts = 10
#grid points
# grdArr =


#build k/d tree index on population
disTreeS = spatial.cKDTree(inXY)
disTreeT = spatial.cKDTree(inT)

#initialize variables
neighSIndex = []    #stores indexes of spatiotemporal neighbors
mNN = np.inf        #minimum number of neighbors
i = 0               # iterator variable

#loop through all data points
while i < numPts:

    #query point
    ptsS = inXY[i]
    ptsT = inT[i]

    #query the tree, input number of neighbors
    neighS = disTreeS.query(ptsS,15)
    neighT = disTreeT.query(ptsT,15)

    #intersect spatial and temporal neighbors
    # a = list(neighS[1])
    # b = set(list(neighT[1]))
    # c = [i for i, item in enumerate(a) if item in b]    #indexes for neighS

    neighST = np.intersect1d(neighS, neighT)

    print(neighST)

    # neighSIndex.append(c)

    #keep track of minimum number of spatiotemporal neighbors
    nSTN = neighST.size #number of space-time neighbors
    if nSTN < mNN:
        mNN = nSTN

    i += 1

print(mNN)

#initiate variables
j = 0

#loop through neighSIndex
# while j < numPts:
#
#     bwS = neighSneighSIndex[minLength]
#
#     j += 1

