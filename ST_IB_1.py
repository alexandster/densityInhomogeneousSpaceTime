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
outFile = open("out_2.txt",'w')

#------------------------------------------------
#build k/d tree index on cases
sTree = spatial.cKDTree(inXYT_s[:,:2])

#------------------------------------------------
#initialize variables
stNeighIndex = []    #stores indexes of spatiotemporal neighbors
mNN = np.inf         # minimum number of neighbors
NN = numPts            # big number: number of nearest neighbors to search for
# neighThres = [5,10,15,20]       # minimum number of ST neighbors threshold

for neighThres in [10]:

    # i = 0              # iterator variable
    i = 200              # iterator variable
    printcounter = 0

    #------------------------------------------------
    #loop through all data points
    while i < numPts:
    # while i < 11001:

        #query point
        sCoord = inXYT_s[i,:2]
        tCoord = inXYT_s[i,2]

        #query the tree, input number of neighbors to search for
        sNeigh = sTree.query(sCoord,NN)

        #temporal neighbors list
        tNeigh = []

        #number of temporal neighbors. procedure ensures that no negative
        #indexes are created.
        if i < NN:
            current = 0
        else:
            current = i - NN

        # append temporal neighbors to list. procedure ensures that only cases from the past are considered.
        # it also deals with cases that co-occur at the same time.
        while inXYT_s[current,2] < inXYT_s[i,2]:
            tNeigh.insert(0,current)
            current += 1

        # print ("len(sNeigh): ", len(sNeigh[0]), "len(tNeigh): ", len(tNeigh))

        # intersect lists of spatial and temporal neighbors. check cardinality. If cardinality is lower than
        # minimum number of ST neighbors threshold, simultaneousely add the next spatial and temporal neighbor
        # from the spatial and temporal neighbor lists, interesect and check cardinality again.
        j = neighThres           #number of spatial and temporal nearest neighbors to consider. at least the minimum number of ST neighbors
        stNeigh = []
        sDistMax = 0            # record maximum distance of farthest spatial neighbor of the intersection set
        tDistMax = 0            # record maximum distance of farthest temporal neighbor of the intersection set
        while len(stNeigh) < neighThres:
            stNeigh = np.intersect1d(list(sNeigh[1][:j]), tNeigh[:j])

            # spatial distance
            sDist = sNeigh[0][j-1]

            # temporal distance. ensuring index k is within range of tNeigh
            if j < len(tNeigh):
                k = j
            else:
                k = len(tNeigh) - 1

            # print(tCoord, inXYT_s[tNeigh[k],2])
            tDist = tCoord - inXYT_s[tNeigh[k],2]
            # print(tDist)

            if sDist > sDistMax:
                sDistMax = sDist
            if tDist > tDistMax:
                tDistMax = tDist
            # print(tDist)

            # print("j: ", j)
            j += 1

        # print("j:", j,"neighThres: ",neighThres,"sDistMax: ", sDistMax, "tDistMax: ", tDistMax)
        # print("stNeigh: ", stNeigh)

        # #write to file
        # s = ", ".join(map(str, list(stNeigh)))
        # outFile.write(str(i) + "," + str(sCoord[0]) + "," + str(sCoord[1]) + "," + str(tCoord) + "," + s + "\n")

        if (printcounter == 100):
            print('Progress ', i)
            printcounter = 0

        printcounter += 1

        outFile.write(str(i) + "," + str(sCoord[0]) + "," + str(sCoord[1]) + "," + str(tCoord) + "," + str(sDistMax) + "," + str(tDistMax) + "\n")

        # #keep track of minimum number of spatiotemporal neighbors
        # nSTN = stNeigh.size #number of space-time neighbors
        # if nSTN < mNN:
        #     mNN = nSTN

        i += 1

# outFile.close()
# print(mNN)
