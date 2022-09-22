from ast import Delete
from pickle import FALSE


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insertNewHeader(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

    def deleteNode(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next


family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
firstkid = Node("Max")
secondKid = Node("Jenny")

family.head.next = wife
wife.next = firstkid
firstkid.next = secondKid

# family.traversal()

family.insertNewHeader("Dave")
# print(family.search("Amy"))
family.deleteNode("Amy")
family.traversal()
