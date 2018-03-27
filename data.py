import random

#population
#------------------------------------------------------------------------------
popFile = open("popdata.txt","w")
i = 0
while i < 100:

    x = random.uniform(0.0,100.0)
    y = random.uniform(0.0,100.0)
    t1 = random.randint(0,99)
    t2 = random.randint(t1,100)
    popFile.write(str(x) + "," + str(y) + "," + str(t1) + "," + str(t2) + "\n")
    i += 1
popFile.close()
#------------------------------------------------------------------------------

#disease cases
#------------------------------------------------------------------------------
casFile = open("casdata.txt","w")
i = 0
while i < 25:

    x = random.uniform(0.0,100.0)
    y = random.uniform(0.0,100.0)
    t = random.randint(0,99)
    casFile.write(str(x) + "," + str(y) + "," + str(t) + "\n")
    i += 1
casFile.close()
#------------------------------------------------------------------------------
