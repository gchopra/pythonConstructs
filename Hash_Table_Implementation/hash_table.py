#This hash table would be using singly linked-list to avoid collison


#Each node would be defined with its key and value and the next node it connects to at that index
class hashNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class hashTable:

    def __init__(self,size):
        self.size = size
        self.table = [None] * size

    #here we will returb hashCode using the key
    def hashiphy(self,key):
        hashed = hash(key) % self.size
        return hashed

    #if there is an entry in the hashtable at the index, we chainlink the keys-values
    def chainHash(self,hashCode,key,val):
        tableNode = self.table[hashCode]

        #look till you find the last entry or a matching key
        while tableNode and tableNode.key != key:
            previousNode, tableNode = tableNode, tableNode.next
        if tableNode: #two values for same key not allowed, so overwrite
            tableNode.val = val
        else:
            tableNode = hashNode(key,val)
            previousNode.next=tableNode


    def get(self,key):
        hashCode = self.hashiphy(key)
        tableNode = self.table[hashCode]
        if tableNode is None:
            print ("no entry found for key=",key)
        else:
            while tableNode and tableNode.key != key:
                tableNode=tableNode.next
            print("entry found key = ", tableNode.key , "value= ",tableNode.val)


    def put(self,key,val):

        hashCode = self.hashiphy(key)
        if self.table[hashCode]:    #if there is an entry in the hash-table at that index
            self.chainHash(hashCode,key,val)
        else:                       #if there is no entry in the hash-table at that index
            self.table[hashCode] = hashNode(key,val)

if __name__ == '__main__':

    #create hash table of size 100
    hashTable = hashTable(100)

    #put some values in the table
    hashTable.put(1,"GAUTAM")
    hashTable.put(2,"IS")
    hashTable.put(20,"DESIGN")
    hashTable.put(4,"VERIFICATION")
    hashTable.put(6,"ENGINEER")

    #read values from the hash table
    hashTable.get(2)
    hashTable.get(1)
    hashTable.get(4)
    hashTable.get(20)
    hashTable.get(6)
    hashTable.get(10)

