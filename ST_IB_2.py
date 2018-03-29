import numpy as np
from scipy import spatial

#------------------------------------------------
#read population file
##popArr = np.loadtxt('popdata.txt',delimiter=',')

#------------------------------------------------
### read case points file
##disFile = open('AllCases2010_11_clip.txt', "r")
##inXYT = []
##disFile.readline()
##for record in disFile:
##    inXYT.append([float(record.split("\t")[0]),float(record.split("\t")[1]),float(record.split("\t")[2])])
##disFile.close()
##numPts = len(inXYT)
##
##inXYT_s = np.array(sorted(inXYT, key=lambda a: a[2]))
##
###------------------------------------------------
###read out_1.txt

inArr = []
inFile = open("out_1.txt", "r")
for line in inFile:
    inLine = []
    for item in line.strip().split(","):
        if item:
            inLine.append(int(item))
    inArr.append(inLine)

print(inArr[:20])
    

