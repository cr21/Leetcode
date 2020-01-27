""""
get the length of Linked list
find the diffrence
traverse longer list with difference

and then taverse both list and check if they meet or not
if they meet then intersection

other aproach :

lets say A is shorter than B then when A reached end point it to original head of B and viceversa B end then point
to original headA , and count it to 2 swap, if they have same before second swap they have intersectiong

"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        #         find the length of HeadA
        count = 0
        OA = headA
        OB = headB
        while headA:
            count += 1
            headA = headA.next
        length_A = count
        count = 0
        while headB:
            count += 1
            headB = headB.next
        lenght_B = count
        count = 0
        diff = abs(lenght_B - length_A)
        if lenght_B > length_A:
            while count < diff:
                print("cuont0")
                OB = OB.next
                count += 1
        else:
            while count < diff:
                OA = OA.next
                count += 1
        while OA:
            if OA == OB:
                return OA

            OA = OA.next
            OB = OB.next

        return None
