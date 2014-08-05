from src.BinaryJSM import BinaryJSM
                
if __name__ == "__main__":
    bjm = BinaryJSM("../input/positive.cxt")
    posIntersections = bjm.formIntersections(bjm.positiveCxt)
    negIntersections = bjm.formIntersections(bjm.negativeCxt)
    print "Intersection 6 covers object 1 from positive set", bjm.intersectionCoversExample(
        posIntersections[5], bjm.positiveCxt.table[0])
    print "Intersection 6 covers object 3 from positive set", bjm.intersectionCoversExample(
        posIntersections[5], bjm.positiveCxt.table[2])
    print "Intersection 5 does not cover objects 3 and 4 from positive set: ", not bjm.intersectionNotCoversSet(
        posIntersections[4], [bjm.positiveCxt.table[2]] + [bjm.positiveCxt.table[3]])
    print "Intersection 6 does not cover objects 3 and 4 from positive set: ", not bjm.intersectionNotCoversSet(
        posIntersections[5], [bjm.positiveCxt.table[2]] + [bjm.positiveCxt.table[3]])
    print "Positive intersection 6 does not cover negative set: ", bjm.intersectionNotCoversSet(
        posIntersections[5], bjm.negativeCxt.table)