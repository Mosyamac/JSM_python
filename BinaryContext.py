import csv
class BinaryContext:
    
    objects, attributes = [], []
    obj_num, attr_num = 0, 0 
    table = []
    
    def parseData(self, cxtFile):
        """
        Parses a cxt file which must have commonly used context file structure:
        -------------
        B
        
        obj_num
        attr_num
        
        {object_names} (each successive one from a new line)
        {attributes} (each successive one from a new line)
        .XX...XXX.
        XXX.XXXX..
        ---------------
        """
        data = csv.reader(open(cxtFile))
        data.next()  # skip line 'B'
        data.next()  # skip empty line 2
        self.obj_num, self.attr_num = int(data.next()[0]), int(data.next()[0])
        data.next()  # skip empty line 5
        self.objects = [data.next()[0] for i in xrange(self.obj_num)]  # @UnusedVariable
        self.attributes = [data.next()[0] for i in xrange(self.attr_num)]  # @UnusedVariable
        self.table = [[1 if i == 'X' else 0 for i in row[0]] for row in data]
        
    def intersect(self, obj_num1, obj_num2):
        """
        for two examples, the intersection is 1 at some position if 1 is in both examples at the 
        corresponding position. Similarly for zero.
        And it is -1 if the values at this position in two examples differ.
        """
        ex1, ex2 = self.table[obj_num1], self.table[obj_num2]
        intersection = [ex1[i] if ex1[i] == ex2[i] else -1 for i in xrange(len(ex1))]
        return intersection
    
    def reprExample(self, example):
        rep = ""
        for i in xrange(len(example)):
            if example[i] == 1:
                rep += self.attributes[i] + ","
        return "[" + rep.strip(",") + "]"
    
if __name__ == "__main__":
    context = BinaryContext()
    context.parseData("input/positive.cxt")
    print "Objects: ", context.objects
    print "Attributes: ", context.attributes
    print "Table: ", context.table
    print context.intersect(0, 1)
    print context.reprExample(context.table[0])
 
        
