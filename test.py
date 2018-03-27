#number of points in each dimension
xDim = 5
yDim = 5
zDim = 5

#block size
nZ = 1
nY = nZ*zDim
nX = nY*yDim

#create the grid
arr = []
count = 0
x = 0
while x < xDim:
    y = 0
    while y < yDim:
        z = 0
        while z < zDim:
            arr.append([x, y, z, count])
            z += 1
            count += 1
        y += 1
    x += 1

#query point
po = [2,2,3]

#neighbor degree
nDeg = 2

#neighbors
pe = [po[0]+nDeg,po[1],po[2]]  #east
pw = [po[0]-nDeg,po[1],po[2]]  #west
pn = [po[0],po[1]+nDeg,po[2]]  #north  
ps = [po[0],po[1]-nDeg,po[2]]  #south
pt = [po[0],po[1],po[2]+nDeg]  #top    
pb = [po[0],po[1],po[2]-nDeg]  #bottom

#array indexing
index_po = po[0]*nX+po[1]*nY+po[2]*nZ
index_pe = pe[0]*nX+pe[1]*nY+pe[2]*nZ
index_pw = pw[0]*nX+pw[1]*nY+pw[2]*nZ
index_pn = pn[0]*nX+pn[1]*nY+pn[2]*nZ
index_ps = ps[0]*nX+ps[1]*nY+ps[2]*nZ
index_pt = pt[0]*nX+pt[1]*nY+pt[2]*nZ
index_pb = pb[0]*nX+pb[1]*nY+pb[2]*nZ


#print
print(arr[index_po],"query point")
print(arr[index_pe],"east")
print(arr[index_pw],"west")
print(arr[index_pn],"north")
print(arr[index_ps],"south")
print(arr[index_pt],"top")
print(arr[index_pb],"bottom")
