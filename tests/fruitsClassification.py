from BinaryJSM import BinaryJSM, CLASSLABELS

if __name__ == "__main__":
    fruits = BinaryJSM("../input/fruits_positive.cxt")
    fruits.formHypotheses()
    print "Positive hypotheses: ", [fruits.reprHypothesis(hyp) for hyp in fruits.positiveHypotheses]
    print "Negative hypotheses: ", [fruits.reprHypothesis(hyp) for hyp in fruits.negativeHypotheses]
    classLabels = fruits.classify("../input/fruits_unknown.cxt")
    for i in xrange(fruits.unknownCxt.obj_num):
        print "Example " + fruits.unknownCxt.objects[i] + " is classified as " + \
        CLASSLABELS[classLabels[i]]