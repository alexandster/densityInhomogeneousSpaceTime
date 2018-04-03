import numpy as np
from scipy import spatial

#------------------------------------------------
#read population file
##popArr = np.loadtxt('popdata.txt',delimiter=',')

#------------------------------------------------
## read case points file
disFile = open('AllCases2010_11_clip.txt', "r")
inXYT = []
disFile.readline()
for record in disFile:
   inXYT.append([float(record.split("\t")[0]),float(record.split("\t")[1]),float(record.split("\t")[2])])
disFile.close()
numPts = len(inXYT)

inXYT_s = np.array(sorted(inXYT, key=lambda a: a[2]))

##------------------------------------------------
##read out_1.txt
inArr = []
inFile = open("out_1.txt", "r")
for line in inFile:
    inLine = []
    for item in line.strip().split(","):
        if item:
            inLine.append(float(item))
    inArr.append(inLine)
###------------------------------------------------


k = 10          #kth neighbor -- how many disease cases support one case
i = 9250         #starting point -- ensure that points have at least k neighbors

stNeigh = []
stNeighDist = []

#loop through inArr, find space-time distance to the kth neighbor
while i < 9251:

    #center point coords
    xC, yC, tC = inArr[i][1],inArr[i][2],inArr[i][3]

    #find kth spatial neighbors
    for j in inArr[i][4:k]:

       xN, yN, tN = inXYT_s[int(j)][0], inXYT_s[int(j)][1], inXYT_s[int(j)][2]
       
       stNeigh.append([xN, yN, tN])
       stNeighDist.append([pow(pow(xC - xN, 2) + pow(yC - yC, 2),0.5), tC - tN])

##    stNeighArr = np.array(stNeigh)

    #find spatial and temporal distance
##    print(stNeighArr)
    
   
    

##    #kth neighbor index
##    kI = int(inArr[i][3+k])
##
##    #kth neighbor coords
##    xN, yN, tN = inXYT_s[kI,0], inXYT_s[kI,1], inXYT_s[kI,2]
##
####    print(xC, yC, tC, xN, yN, tN)
##
##    sDist = pow(pow(xC - xN, 2) + pow(yC - yN, 2), 0.5)
##    tDist = tC - tN
##
##    print("center coord", xC, yC, tC, "kth neighbor coords", xN, yN, tN, "dist", sDist, tDist)

    i += 1
