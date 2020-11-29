# coding=utf-8
class Node():
    def __init__(self,length,children=None,left=None,right=None):
        self.length = length
        self.children = children
        self.left = left
        self.right = right





class hdfsTree():

    def __init__(self,root=None):
        self.root = root
        self.tree = None

    def set_tree(self,tree):
        self.tree = tree

    def isEmpty(self):
        return self.root == None

    def lengthTree(self):
        if self.isEmpty():
            return 0

    def insert(self,node:Node):
        """

        :type node: hdfsNode
        """
        if self.isEmpty():
            self.root = node
            return

        hn = self.root
        while True:
            if node.length <= hn.length:
                if hn.left == None:
                    hn.left = node
                    return
                else:
                    hn = hn.left
            else:
                if hn.right == None:
                    hn.right = node
                    return
                else:
                    hn = hn.right

    def nprint(self):
        if self.isEmpty():
            print("这是空的")
            return

        def nnprint(node:Node,position):
            print("值：%d，方位：%s"%(node.length,position))
            if node.left: nnprint(node.left,"left")
            if node.right: nnprint(node.right,"right")

        nnprint(self.root,"root")

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    n4 = Node(2)

    hn = hdfsTree()
    hn.insert(n1)
    hn.insert(n2)
    hn.insert(n3)
    hn.insert(n4)

    hn.nprint()
