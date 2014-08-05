from BinaryJSM import BinaryJSM
                
if __name__ == "__main__":
    fruits = BinaryJSM("../input/positiveFruits.cxt")
    fruits.formHypotheses()
    print fruits.positiveHypotheses
    print [fruits.reprHypothesis(hyp) for hyp in fruits.positiveHypotheses]