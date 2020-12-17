class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert_root_value(self, key=None):
        self.key = key

    def insert_left(self, key=None):
        self.left = TreeNode(key, self.left)

    def insert_right(self, key=None):
        self.right = TreeNode(key, None, self.right)

    def get_root_value(self):
        return self.key

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def inorder(self):
        if self.get_left_child() is not None:
            self.get_left_child().inorder()
        print(self.key, end=", ")
        if self.get_right_child() is not None:
            self.get_right_child().inorder()

    def preorder(self):
        print(self.key, end=", ")
        if self.get_left_child() is not None:
            self.get_left_child().preorder()
        if self.get_right_child() is not None:
            self.get_right_child().preorder()

    def postorder(self):
        if self.get_left_child() is not None:
            self.get_left_child().postorder()
        if self.get_right_child() is not None:
            self.get_right_child().postorder()
        print(self.key, end=", ")
