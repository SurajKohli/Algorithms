# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

    # Utility function to prit the linked LinkedList
    def printList(self, node):
        temp = node
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def getHead(self):
        return self.head

def getSizeOfList(head):
    size = 0
    while( head != None ):
        size = size + 1
        head = head.next
    return size

def removeNode(prev,head):
    prev.next = head.next
    head.next = None

def deleteMiddle(head):
    main_head = head
    # check even/odd
    # for odd remove middle, for even remove 2nd middle
    size = getSizeOfList(head)
    if( size == 0 or size == 1 ):
        return None

    for i in range(size//2):
        prev = head
        head = head.next
    removeNode(prev,head)

    #function to return new head of deleted list
    return main_head

# Driver program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lst=LinkedList()
        for i in arr:
            lst.push(i)
        newhead = None
        # deleteMiddle(lst.getHead())
        newhead = deleteMiddle(lst.getHead())
        print("---")
        lst.printList(newhead)
        print("\n---")
