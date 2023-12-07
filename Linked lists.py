#This is class that represents a single node. This node does not lead to anything so the next variable is set to none. 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

#This is a class for the Linked list. It stores the methods that give the LL its functionality
class LinkedList:
    def __init__(self, nodes = None):
        self.head = None

        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node

            for elements in nodes:
                node.next = Node(data = elements)
                node = node.next
    
    #method to iterate over the linked list
    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    
    #default thing to do when LL is called. 
    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        
        nodes.append('None')

        return "->".join(nodes)
    

    #To add to the beginning of the LL
    def add_first(self, node):
        newNode = Node(node)

        newNode.next = self.head
        self.head = newNode
    
    #To add to the end of the LL
    def add_end(self, node):
        newNode = Node(node)

        if self.head is None:
            self.head = node
            return

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            
            current_node.next = newNode

    
    #To add between two target elements in the LL    
    def add_between(self, taget_start_node, target_end_node, new_node):

        newNode = Node(new_node)

        if self.head is None:
            self.head = newNode
            return
        
        else:
            target_start = None
            target_end = None
            currentNode = self.head

            while currentNode.next is not None:
                if currentNode.data == taget_start_node:
                    target_start = currentNode
                
                if currentNode.data == target_end_node:
                    target_end = currentNode
                
                currentNode = currentNode.next
                
            newNode.next = target_end
            target_start.next = newNode
                

    #To get the index of a specific element in the linked list              
    def get_index(self, target_node):
        count = 0
        currentNode = self.head

        while currentNode.next is not None:
            if currentNode.data == target_node:
                print(count)
            else:
                count += 1

            currentNode = currentNode.next
        
    
    def replace(self, target_node, new_node):
        newNode = Node(new_node)
        currentNode = self.head

        while currentNode.next is not None:

            if currentNode.data == target_node:
                currentNode = newNode
                newNode.next = currentNode.next
            
            currentNode = currentNode.next

    

#initializing the objects for the linked list
LL = LinkedList()

firstNode = Node('a')
LL.head = firstNode

secondNode = Node('b')
thirdNode = Node('c')
fourthNode = Node('d')


firstNode.next = secondNode
secondNode.next = thirdNode
thirdNode.next = fourthNode

LL.add_first('k')
LL.add_end('H')
LL.add_between('c','d','z')

LL.get_index('a')
LL.replace('a','I')

print(LL)