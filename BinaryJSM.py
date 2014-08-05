from BinaryContext import BinaryContext

CLASSLABELS = {1:"positive", 0:"negative", -1:"undefined"}

class BinaryJSM:
    
    positiveCxt, negativeCxt = BinaryContext(), BinaryContext()
    unknownCxt = BinaryContext()
    positiveHypotheses, negativeHypotheses = [], []
    
    def __init__(self, posCxtFile):
        self.positiveCxt.parseData(posCxtFile)
        self.negativeCxt.parseData(posCxtFile.replace("positive", "negative"))
        
    def formIntersections(self, cxt):
        intersections = []
        for obj_num1 in xrange(len(cxt.table)):
            for obj_num2 in xrange(obj_num1 + 1, len(cxt.table)):
                intersections.append(cxt.intersect(obj_num1, obj_num2))
        return intersections
    
    def intersectionCoversExample(self, intersection, example):
        """
        Checks if an intersection covers an example
        For instance, [0,-1,1,-1] covers [0,1,1,0]
        (minus 1 might be treated as either 0 or 1)
        But [1,-1,1,0] does not cover [1,0,0,0]
        """
        for i in xrange(len(intersection)):
            if intersection[i] == 1 and example[i] == 0:
                return False
        return True
    
    def intersectionNotCoversSet(self, intersection, objectSet):
        """
        Checks if an intersection covers all examples from objectSet
        For instance, [0,-1,1,-1] covers a set [[0,1,1,0], [0,0,1,0]]
        (minus 1 might be treated as either 0 or 1)
        But [1,-1,1,0] does not cover a set [[1,0,0,0],[1,0,1,0]]
        """
        for example in objectSet:
            if self.intersectionCoversExample(intersection, example):
                return False
        return True
    
    def formHypotheses(self):
        positiveIntersections = self.formIntersections(self.positiveCxt)
        negativeIntersections = self.formIntersections(self.negativeCxt)
        positiveHypotheses, negativeHypotheses = [], []
        for intersection in positiveIntersections:
            if self.intersectionNotCoversSet(intersection, self.negativeCxt.table):
                positiveHypotheses.append(intersection)                
        for intersection in negativeIntersections:
            if self.intersectionNotCoversSet(intersection, self.positiveCxt.table):
                negativeHypotheses.append(intersection)
        self.positiveHypotheses = positiveHypotheses
        self.negativeHypotheses = negativeHypotheses
    
    def classify(self, unknownCxtFile):
        """
        Classifies  examples with unknown labels from unknownCxtFile
        If the number of positive hypotheses covered by the description of
        the example (votingPositiveNum) is equal to the the number of negative
        hypotheses covered by the description of the example, then the example 
        is classified as undefined.
        Otherwise, its label is the result of the voting procedure.
        """
        labels = []
        self.unknownCxt.parseData(unknownCxtFile)
        positiveCoverage = [[self.intersectionCoversExample(posHyp, testObject)
                             for posHyp in self.positiveHypotheses] 
                             for testObject in self.unknownCxt.table]
        negativeCoverage = [[self.intersectionCoversExample(negHyp, testObject)
                             for negHyp in self.negativeHypotheses] 
                             for testObject in self.unknownCxt.table]
        for i in xrange(len(positiveCoverage)):
            votingPositiveNum = sum(positiveCoverage[i])
            votingNegativeNum = sum(negativeCoverage[i])
            labels.append(-1) if votingPositiveNum == votingNegativeNum  \
                            else labels.append(int(votingPositiveNum > votingNegativeNum)) 
        return labels            
        
    def reprHypothesis(self, hypothesis):
        rep = ""
        for i in xrange(len(hypothesis)):
            if hypothesis[i] == 1:
                rep += self.positiveCxt.attributes[i] + ","
        return "<" + rep.strip(",") + ">"
                
if __name__ == "__main__":
    fruits = BinaryJSM("input/positiveFruits.cxt")
    fruits.formHypotheses()
    print "Positive hypotheses: ", [fruits.reprHypothesis(hyp) for hyp in fruits.positiveHypotheses]
    print "Negative hypotheses: ", [fruits.reprHypothesis(hyp) for hyp in fruits.negativeHypotheses]
    classLabels = fruits.classify("input/unknownFruits.cxt")
    for i in xrange(fruits.unknownCxt.obj_num):
        print "Example " + fruits.unknownCxt.objects[i] + " is classified as " + \
        CLASSLABELS[classLabels[i]]
        
