

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


if __name__ == '__main__':
    list = linkedList()
    list.head = node(10)
    node_2 = node(20)
    node_3 = node(30)

    list.head.next = node_2
    node_2.next = node_3

    #print the whole Linked List moving through it
    list.printList()
