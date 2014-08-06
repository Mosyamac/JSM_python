from BinaryJSM import BinaryJSM, CLASSLABELS

if __name__ == "__main__":
    adults = BinaryJSM("../input/adults_positive.cxt")
    adults.formHypotheses()
    print "Positive hypotheses: ", [adults.reprHypothesis(hyp) for hyp in adults.positiveHypotheses]
#     print "Negative hypotheses: ", [adults.reprHypothesis(hyp) for hyp in adults.negativeHypotheses]
#     classLabels = adults.classify("../input/positiveTestAdults.cxt")
#     for i in xrange(adults.unknownCxt.obj_num):
#         print "Example " + adults.unknownCxt.objects[i] + " is classified as " + \
#         CLASSLABELS[classLabels[i]]