class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        link = self.head
        while link:
            print(link.data)
            link = link.next


    #Add a node at the end
    def append(self,data):
        appendNode = node(data)

        #if it's a empty linkedlist
        if self.head is None:
            self.head=appendNode
        else:
            endNode = self.head
            while endNode.next:
                endNode=endNode.next
            endNode.next=appendNode

    #add a node at the beginning
    def push(self,data):
        pushNode = node(data)
        pushNode.next=self.head
        self.head=pushNode

    # add a node after a node
    def pushAfter(self,nodeNumber, data):
        pushNode = node(data)

        #if it's a empty linkedlist
        if self.head is None:
            self.head=pushNode

        link = self.head
        for i in range(nodeNumber-1):
            link=link.next
            if (link.next is None): break

        pushNode.next = link.next
        link.next=pushNode


if __name__ == '__main__':
    lList = linkedList()
    lList.append(10)
    lList.push(20)
    lList.append(30)
    lList.append(40)
    lList.pushAfter(3,50)


    #print the whole Linked List moving through it
    lList.printList()