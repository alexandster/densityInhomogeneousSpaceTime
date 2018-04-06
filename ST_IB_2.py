import numpy as np
from scipy import spatial

#------------------------------------------------
#read population files, add them to one array
i = 0
popList = []
while i <  334:
    popFile = open("pop_model_out/barrio_" + str(i) + ".txt", "r")
    for record in popFile:
        x, y, tStart, tEnd = record.split(",")
        popList.append([float(x),float(y),int(tStart),int(tEnd.strip())])
    popFile.close()
    i += 1

# print(popList[0])
popArr = np.array(popList)

#------------------------------------------------
## read file containing case coordinates and bandwidths
disFile = open('out_2.txt', "r")
disList = []
for record in disFile:
    line = record.split(",")
    disList.append([float(line[0]),float(line[1]),float(line[2]),float(line[3]),float(line[4]),float(line[5])])
disFile.close()
numPts = len(disList)

#------------------------------------------------
# open output File
outFile = open("out_3.txt",'w')

#------------------------------------------------
# define get overlap function. returns overlap between two intervals.
def getOverlap(a, b):
    return max(0, min(a[1], b[1]) - max(a[0], b[0]))

#------------------------------------------------

#build kd tree
sTree = spatial.cKDTree(popArr[:,:2])

printcounter = 0
count = 0
#for each disease case, compute populaiton inside kernel, compute diease risk contribution to grid points within the kernel
for i in disList:

    sCoord = i[1:3]
    # query the tree: return all population points within bandwidth
    sNeigh = sTree.query_ball_point(sCoord, i[4])

    #check whether neighbors exist within bandwidth
    # if len(sNeigh) == 0:
    #     print("nope")
    # else:
    #     print(sNeigh)

    pt = 0      #people-time: how many people present inside kernel for how long? population adjustment.
    # for each population neighbor, calculate length of stay within kernel
    for j in sNeigh:
        popStart = popArr[j,2]      #start of population column
        popEnd = popArr[j,3]        #end of population column
        kerEnd = i[3]               #end of kernel (=time of disase case)
        kerStart = kerEnd - i[5]    #start of kernel (=time of disease case minus temporal bandwidth)
        pt += getOverlap([popStart,popEnd],[kerStart,kerEnd])

    outFile.write(str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(i[5]) + "," + str(pt) + "\n")

    if (printcounter == 100):
        print('Progress ', count)
        printcounter = 0

    printcounter += 1
    count += 1

outFile.close()

        # print(popStart, popEnd, kerStart, kerEnd, los)

    # print(i[1:3], i[4], len(sNeigh))




# np.savetxt("popArr.txt", popArr, delimiter=',')

# inXYT_s = np.array(sorted(inXYT, key=lambda a: a[2]))



# k = 10          #kth neighbor -- how many disease cases support one case
# i = 5000         #starting point -- ensure that points have at least k neighbors
#
# #loop through inArr, find space-time distance to the kth neighbor
# while i < 5050:
#
#     #center point coords
#     xC, yC, tC = inArr[i][1],inArr[i][2],inArr[i][3]
#
#     #kth neighbor index
#     kI = int(inArr[i][3+k])
#
#     #kth neighbor coords
#     xN, yN, tN = inXYT_s[kI,0], inXYT_s[kI,1], inXYT_s[kI,2]
#
#     # print(xC, yC, tC, xN, yN, tN)
#
#     sDist, tDist = pow(pow(xC - xN, 2) + pow(yC - yC, 2),0.5), tC - tN
#
#     print (sDist, tDist)
#
#     i += 1
