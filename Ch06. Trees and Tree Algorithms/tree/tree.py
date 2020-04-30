
class Node: 
    def __init__(self, key = None, parent = None):
        self.key = key
        self.parent = parent
        self.children: dict = {}

    
class Tree:
    def __init__(self, key = None):
        self.root: Node = Node(key)

    def height(self)->int:
        return self.__height__(self.root)

    def __height__(self, node: Node)->int:
        if node is None or node.key is None:
            return 0
        elif len(node.children) == 0:
            return 1
        else:
            heights: list = []
            for key in node.children:
                heights.append(self.__height__(node.children[key]))
            return 1 + max(heights)

    def getNode(self, key)->Node:
        if self.root is None or self.root.key is None:
            return None
        elif self.root.key == key:
            return self.root
        else:
            tmp: Node = None
            for childKey in self.root.children:
                tmp = self.__getNode__(self.root.children[childKey], key)
                if tmp is not None:
                    break
            if tmp is not None:
                return tmp
            else:
                raise Exception("Node with key " + str(key) + " not found")
    
    def __getNode__(self, node: Node, key)->Node:
        if node.key == key:
            return node
        else:
            tmp: Node = None
            for childKey in node.children:
                tmp = self.__getNode__(node.children[childKey], key)
                if tmp is not None:
                    break
            return tmp

    def contains(self, key)->bool:
        self.getNode(key) # will throw Eception if node doesn't exist
        return True

    def insert(self, key1, key2):
        if key1 is None or key2 is None:
            return
        parent: Node = self.getNode(key1)
        if parent is not None and parent.key != key2:
            parent.children[key2] = Node(key2, parent)

tree: Tree = Tree(1)
tree.insert(1, 10)
tree.insert(1, 2)
tree.insert(1, 7)

tree.insert(2, 22)
tree.insert(2, 29)
tree.insert(29, 229)
tree.insert(229, 2229)


tree.insert(7, 77)
tree.insert(7, 71)
tree.insert(7, 719)

print(tree.height())
print(tree.getNode(29).key)
print(tree.getNode(2229).key)
print(tree.getNode(11).key)






