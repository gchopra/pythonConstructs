#This is a double ended queue using list type

class DE_queue:
    def __init__(self ):
        self.q = [] #create an empty list that will be the queue

    def pushFrontQ(self,object):
        self.q.insert(0,object)

    def popFrontQ(self):
        self.q.pop(0)

    def pushRearQ(self,object):
        self.q.append(object)

    def popRearQ(self):
        self.q.pop()

    def printQ(self):
        for i in self.q: print(i)

    def sizeQ(self):
        return len(self.q)

if __name__ == '__main__':

    queue = DE_queue()
    queue.pushFrontQ(10)
    queue.pushFrontQ(20)
    queue.pushFrontQ(30)
    queue.printQ()
    print("size before pop:",queue.sizeQ())

    queue.popFrontQ()
    queue.printQ()
    print("size after pop:",queue.sizeQ())

    queue.popRearQ()
    queue.printQ()
    print("size after pop:",queue.sizeQ())
