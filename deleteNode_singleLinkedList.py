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


    def deleteNode(self,nodeValue):

        link = self.head

        #if its the first node
        if(link is not None):
            if link.data==nodeValue:
                self.head=link.next
                link = None #delete the node
                return

        while (link is not None):
            if link.data == nodeValue:
                break
            else:
                prevNode = link
                link = link.next
        if link is None: return
        prevNode.next = link.next
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
    print ("after deletion")
    lList.printList()


