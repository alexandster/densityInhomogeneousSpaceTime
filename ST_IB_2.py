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
i = 250         #starting point -- ensure that points have at least k neighbors

#loop through inArr, find space-time distance to the kth neighbor
while i < 270:

    #center point coords
    xC, yC, tC = inArr[i][1],inArr[i][2],inArr[i][3]

    #kth neighbor index
    kI = int(inArr[i][3+k])

    #kth neighbor coords
    xN, yN, tN = inXYT_s[kI,0], inXYT_s[kI,1], inXYT_s[kI,2]

    print(xC, yC, tC, xN, yN, tN)

    # dist =

    i += 1
