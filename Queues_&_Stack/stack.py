#We create the LIFO stack using a list

class stack:
    def __init__(self ):
        self.stack = [] #create an empty list that will be the queue

    def pushStack(self,object):
        self.stack.insert(0,object)

    def popStack(self):
        self.stack.pop(0)

    def printStack(self):
        for i in self.stack: print(i)

    def sizeStack(self):
        return len(self.stack)

if __name__ == '__main__':

    s = stack()
    s.pushStack(10)
    s.pushStack(20)
    s.pushStack(30)
    s.pushStack(40)
    s.printStack()
    print("size before pop:",s.sizeStack())

    s.popStack()
    s.printStack()
    print("size after pop:",s.sizeStack())
