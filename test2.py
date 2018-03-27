#global stuff
#--------------------------------------------------------------------
#spatiotemporal domain
xmin, xmax, ymin, ymax, zmin, zmax = 10, 15, 10, 15, 10, 15

#create the grid
arr = []
count = 0
x = xmin
while x < xmax:
    y = ymin
    while y < ymax:
        z = zmin
        while z < zmax:
            arr.append([x, y, z, count])
            z += 1
            count += 1
        y += 1
    x += 1
print "#gridpoints", len(arr)

#function def
#--------------------------------------------------------------------
#xmin, xmax, ymin, ymax, zmin, zmax: spatiotemporal domain
#qX, qY, qZ: query point coordinates
#nDeg: neighbor degree
def neighST(xmin, xmax, ymin, ymax, zmin, zmax, qX, qY, qZ, nDeg):

    #number of points in each dimension
    xDim = xmax - xmin
    yDim = ymax - ymin
    zDim = zmax - zmin

    #block size
    nZ = 1
    nY = nZ*zDim
    nX = nY*yDim
    
    count = 0
    #produce list of indexes of neighbors
    nil = []        #neighbor index list
    for i in range(qX-nDeg,qX+nDeg):
        if i < xDim and i >= 0:
            for j in range(qY-nDeg,qY+nDeg):
                if j < yDim and j >= 0:
                    for k in range(qZ-nDeg,qZ+nDeg):
                        if k < zDim and k >= 0:
                            nil.append(arr[i*nX+j*nY+k*nZ])
                            count += 1
    print "#neighbors", count
    return nil

#function call
#--------------------------------------------------------------------
print neighST(xmin, xmax, ymin, ymax, zmin, zmax , 1, 2, 2, 2)

