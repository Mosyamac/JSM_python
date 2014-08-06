from fca import ManyValuedContext
from fca.readwrite.comma_separated import read_mv_csv

class IntervalJSM:
    
    positiveCxt, negativeCxt = ManyValuedContext(), ManyValuedContext()
    positiveHypotheses, negativeHypotheses = [], []
    
    def __init__(self, posCxtFile):
        self.positiveCxt = read_mv_csv(posCxtFile)
        self.negativeCxt = read_mv_csv(posCxtFile.replace("positive","negative"))
        
    def formIntersections(self, cxt):
        intersections = []
        for obj_num1 in xrange(len(cxt._table)):
            for obj_num2 in xrange(obj_num1+1, len(cxt._table)):
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
        
    def reprHypothesis(self, hypothesis):
        rep = ""
        for i in xrange(len(hypothesis)):
            if hypothesis[i] == 1:
                rep += self.positiveCxt.attributes[i] + ","
        return "<" + rep.strip(",") + ">"
                
if __name__ == "__main__":
    weather = IntervalJSM("../input/weather_positive.csv")
#     print weather.__dict__
    print weather.negativeCxt.__dict__
    weather.formHypotheses()
#     print "Positive hypotheses: ", [weather.reprHypothesis(hyp) for hyp in weather.positiveHypotheses]
#     print "Negative hypotheses: ", [weather.reprHypothesis(hyp) for hyp in weather.negativeHypotheses]
        