# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def prepend(self, value):
#         """ Prepend a value to the beginning of the list. """
#
#         # TODO: Write function to prepend here
#
#         if  self.head is not None:
#             currenthead = self.head
#             self.head = Node(value)
#             self.head.next = currenthead
#         else:
#             self.head=Node(value)
#
#         pass
#
#     def append(self, value):
#         """ Append a value to the end of the list. """
#
#         # TODO: Write function to append here
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         tail = self.head
#         while(tail.next):
#             tail = tail.next
#         tail.next = new_node
#
#     def search(self, value):
#         """ Search the linked list for a node with the requested value and return the node. """
#
#         # TODO: Write function to search here
#
#         currentNode = self.head
#         if value == self.head.value:
#             return self.head
#         else:
#             while (currentNode.next):
#                 if currentNode.next.value == value:
#                     return currentNode.next
#                 currentNode = currentNode.next
#             return None
#
#     def remove(self, value):
#         """ Remove first occurrence of value. """
#
#         # TODO: Write function to remove here
#         if self.head is None :
#             return
#
#         if self.head.value == value:
#             self.head =self.head.next
#             return
#         prev = self.head
#         current = self.head
#         while(current):
#             # print("{} current  {} prev {} next".format(prev.value,current.value,current.next.value))
#             if current.value == value:
#                 if current.next is not None:
#                     prev.next = current.next
#                 else :
#                     prev.next=None
#                 return
#             prev = current
#             if current.next is not None:
#                 current =current.next
#             else:
#                 current=None
#
#     def pop(self):
#         """ Return the first node's value and remove it from the list. """
#         if self.head is None :
#             return None
#         if self.head.next is not None:
#             updatedhead = self.head.next
#             value=self.head.value
#             self.remove(value)
#             self.head = updatedhead
#             return value
#
#     def insert(self, value, pos):
#         """ Insert value at pos position in the list. If pos is larger than the
#             length of the list, append to the end of the list. """
#
#         # TODO: Write function to insert here
#         if pos >= self.size():
#             self.append(value)
#             return
#         if pos == 0:
#             self.prepend(value)
#             return
#         new_node = Node(value)
#         current = self.head
#         prev = self.head
#         count=0
#         while current.next and count <=pos :
#             if count == pos:
#                 prev.next = new_node
#                 new_node.next=current
#                 return
#             prev = current
#             current = current.next
#             count+=1
#
#
#     def size(self):
#         """ Return the size or length of the linked list. """
#
#         # TODO: Write function to get size here
#
#         currentNode = self.head
#         size=1
#         while(currentNode.next):
#             size += 1
#             currentNode = currentNode.next
#         return size
#     def to_list(self):
#         out = []
#         node = self.head
#         while node:
#             out.append(node.value)
#             node = node.next
#         return out
# linkedList =LinkedList()
# linkedList.append(3)
# linkedList.append(2)
# linkedList.append(0)


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        turtule = head
        hair = head




        while hair != None:
            if hair.next is None:
                return False

            elif turtule.next == turtule:
                return True
            else:
                hair = hair.next.next
                turtule = turtule.next

            if hair == turtule:
                return  True

        return False