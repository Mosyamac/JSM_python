from BinaryJSM import BinaryJSM
                
if __name__ == "__main__":
    fruits = BinaryJSM("../input/fruits_positive.cxt")
    fruits.formHypotheses()
    print "Positive hypotheses: ", [fruits.reprHypothesis(hyp) for hyp in fruits.positiveHypotheses]
    print "Negative hypotheses: ", [fruits.reprHypothesis(hyp) for hyp in fruits.negativeHypotheses]