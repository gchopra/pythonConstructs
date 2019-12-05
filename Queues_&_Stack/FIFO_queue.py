
#We create the FIFO queue using a list

class queue:
    def __init__(self ):
        self.q = [] #create an empty list that will be the queue

    def pushQ(self,object):
        self.q.insert(0,object)

    def popQ(self):
        self.q.pop()

    def printQ(self):
        for i in self.q: print(i)

    def sizeQ(self):
        return len(self.q)

if __name__ == '__main__':

    queue = queue()
    queue.pushQ(10)
    queue.pushQ(20)
    queue.pushQ(30)
    queue.pushQ(40)
    queue.printQ()
    print("size before pop:",queue.sizeQ())

    queue.popQ()
    queue.printQ()
    print("size after pop:",queue.sizeQ())

