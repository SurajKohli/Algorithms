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
    new_head = head.next
    prev.next = head.next
    head.next = None
    return new_head

def removeDuplicates(head):
    main_head = head
    # one pass over the LL O(n)
    if( head == None ):
        return None
    # space => O(max_element)
    # instead of array use hashmap
    # temp_list = [0] * 100
    hash_map = {}
    prev = head
    while( head != None ):
        # keep adding it to temp array
        # if( temp_list[head.data] == 1 ):
        if head.data in hash_map:
            # remove node and return head pointer to next element
            head = removeNode(prev,head)
        else:
            prev = head
            # temp_list[head.data] = 1
            hash_map[head.data] = 1
            head = head.next
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
        newhead = removeDuplicates(lst.getHead())
        print("---")
        lst.printList(newhead)
        print("\n---")
