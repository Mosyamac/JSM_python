def makeCxtFile(f, table):
    obj_num, attr_num = len(table), len(table[0])
    print >> f, "B"
    print  >> f, ""
    print >> f, obj_num
    print >> f, attr_num
    print  >> f, ""
    for i in xrange(obj_num):
        print >> f, i+1
    for i in xrange(attr_num):
        print >> f, i+1
    for item in table:
        print >> f, item    

def parseData(filename):
    f = open(filename)
    posCxt, negCxt = [], []
    for line in f:
        line  = line.strip().split()
        target = int(line[0])
        indices = [int(el.split(":")[0]) for el in line[1:]]
        newLine = ""
        for i in xrange(120):
            newLine += ("X" if i in indices else ".")
        if target == 1:
            posCxt.append(newLine)
        elif target == -1:
            negCxt.append(newLine)
    return posCxt, negCxt

posCxt, negCxt = parseData("../input/a1a")
posCxtFile = open("../input/positiveAdults.cxt",'w')
negCxtFile = open("../input/negativeAdults.cxt",'w')
makeCxtFile(posCxtFile, posCxt)
makeCxtFile(negCxtFile, negCxt)

posTestCxt, negTestCxt = parseData("../input/a1a.t")
posTestCxtFile = open("../input/positiveTestAdults.cxt",'w')
negTestCxtFile = open("../input/negativeTestAdults.cxt",'w')
makeCxtFile(posTestCxtFile, posTestCxt)
makeCxtFile(negTestCxtFile, negTestCxt)
  

        
        