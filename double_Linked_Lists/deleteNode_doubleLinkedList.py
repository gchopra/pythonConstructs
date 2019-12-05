class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous = None


class linkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        link = self.head

        print("In forward direction")
        while link:
            print(link.data)
            finalNode = link
            link = link.next

        print("In reverse direction")
        while finalNode:
            print(finalNode.data)
            finalNode = finalNode.previous

    #Add a node at the end
    def append(self,data):
        appendNode = node(data)

        # as  its the last node, make the next node as none
        appendNode.next = None

        #if it's a empty linkedlist
        if self.head is None:
            appendNode.previous=None
            self.head=appendNode
        else:
            endNode = self.head
            while endNode.next:
                endNode=endNode.next
            endNode.next=appendNode
            appendNode.previous=endNode


    def deleteNode(self,nodeValue):

        link = self.head

        #if its the first node
        if(link is not None):
            if link.data==nodeValue:
                self.head=link.next
                link.next.previous = None
                link = None #delete the node
                return

        while (link is not None):
            if link.data == nodeValue:
                break
            else:
                link = link.next
        if link is None: return
        link.previous.next = link.next
        link.next.previous=link.previous
        link = None #delete the node



if __name__ == '__main__':
    lList = linkedList()
    lList.append(10)
    lList.append(20)
    lList.append(30)
    lList.append(40)
    print ("before deletion")
    lList.printList()
    lList.deleteNode(10)
    lList.deleteNode(30)
    print ("after deletion")
    lList.printList()

