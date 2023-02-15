class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):

        if root is None:

            return -1
        else:
            l = self.getHeight(root.left)
            r = self.getHeight(root.right)

            return max(l, r) + 1

        # Write your code here


T = int(input())