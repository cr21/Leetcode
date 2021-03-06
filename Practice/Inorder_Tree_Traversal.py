""""
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.



             1
          /   \
        2      3
      /  \
    4     5
Output -> 4->2->5->1->3

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        visited = []

        current = root
        # stack.append(root.val)
        while True:

            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                visited.append(current.val)
                current = current.right
            else:
                break
        return visited




""""
Step 1: Initialize current as root

Step 2: While current is not NULL,

If current does not have left child

    a. Add current’s value

    b. Go to the right, i.e., current = current.right

Else

    a. In current's left subtree, make current the right child of the rightmost node
    find inorder predecessor of current and point inorderpredessor.right =current
    b. Go to this left child, i.e., current = current.left  

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> visited = new ArrayList<>();
        
        TreeNode current = root;
            TreeNode predessor;
        while( current != null){
            if(current.left == null){
                visited.add(current.val);
                current = current.right;
            }
            else{
                 predessor = current.left;
                while (predessor.right !=  current && predessor.right != null){
                    predessor = predessor.right;
                }
                if (predessor.right == null){
                    predessor.right = current;
                    current = current.left;
                }else{
                    visited.add(current.val);
                    predessor.right = null;
                    current=current.right;        
                }
            }
        }
        System.out.print(visited.toString());
        return visited;
            
        
    }
}




"""