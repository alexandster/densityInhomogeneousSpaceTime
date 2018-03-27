import numpy as np
from scipy import spatial

#population
popArr = np.loadtxt('popdata.txt',delimiter=',') 

#disease cases
# disArr = np.loadtxt('casdata.txt',delimiter=',')

# read input point file
# disFile = open('casdata.txt', "r")
disFile = open('AllCases2010_11_clip.txt', "r")
inXY, inT = [], []
for record in disFile:
    inXY.append([float(record.split("\t")[0]),float(record.split("\t")[1])])
    inT.append([float(record.split("\t")[2])])
disFile.close()
numPts = len(inXY)

#grid points
# grdArr =


#build k/d tree index on population
disTreeS = spatial.cKDTree(inXY)
disTreeT = spatial.cKDTree(inT)

#initialize variables
neighSIndex = []    #stores indexes of spatiotemporal neighbors
minLength = np.inf  #minimum number of neighbors
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
    a = list(neighS[1])
    b = set(list(neighT[1]))
    c = [i for i, item in enumerate(a) if item in b]    #indexes for neighS

    print(a, b, c)

    neighSIndex.append(c)

    #keep track of minimum number of spatiotemporal neighbors
    if len(c) < minLength:
        minLength = len(c)

    i += 1

print(minLength)

#initiate variables
j = 0

#loop through neighSIndex
# while j < numPts:
#
#     bwS = neighSneighSIndex[minLength]
#
#     j += 1

