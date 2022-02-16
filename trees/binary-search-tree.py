class TreeNode:
    def __init__(self, key=None, value=None, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def has_left_child(self) -> bool:
        return self.left is not None

    def has_right_child(self) -> bool:
        return self.right is not None

    def has_both_children(self) -> bool:
        return self.has_left_child() and self.has_right_child()

    def is_leaf(self) -> bool:
        return not self.has_left_child() and not self.has_right_child()

    def is_root(self) -> bool:
        return self.parent is None

    def has_parent(self) -> bool:
        return self.parent is not None

    def is_left_child(self) -> bool:
        if self.parent is None:
            return False
        return self.parent.left == self

    def is_right_child(self) -> bool:
        if self.parent is None:
            return False
        return self.parent.right == self

    def find_min(self):
        if self is None:
            return None
        if self.has_left_child():
            return self.left.find_min()
        else:
            return self

    def find_max(self):
        if self is None:
            return None
        node = self
        while node.right is not None:
            node = node.right
        return node


class BinarySearchTree:
    def __init__(self):
        self.root: TreeNode = None
        self.elements: int = 0

    def size(self) -> int:
        return self.elements

    def is_empty(self) -> bool:
        return self.root is None

    def put(self, key, value):
        if self.is_empty():
            self.root = TreeNode(key, value)
            self.elements += 1
        else:
            self._put(self.root, key, value)

    def _put(self, root: TreeNode, key, value):
        if root.key == key:
            root.value = value
        elif key < root.key:
            if root.has_left_child():
                self._put(root.left, key, value)
            else:
                root.left = TreeNode(key, value, root)
                self.elements += 1
        else:
            if root.has_right_child():
                self._put(root.right, key, value)
            else:
                root.right = TreeNode(key, value, root)
                self.elements += 1

    def get(self, key) -> TreeNode:
        if self.is_empty():
            return None
        else:
            return self._get(self.root, key)

    def _get(self, root: TreeNode, key) -> TreeNode:
        if root.key == key:
            return root
        elif key < root.key:
            if root.has_left_child():
                return self._get(root.left, key)
            else:
                return None
        else:
            if root.has_right_child():
                return self._get(root.right, key)
            else:
                return None

    def contains(self, key) -> bool:
        if self.is_empty():
            return False
        found: bool = False
        node: TreeNode = self.root
        while node is not None and not found:
            if node.key == key:
                found = True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return found

    def delete(self, key):
        node_to_delete: TreeNode = self.get(key)
        if node_to_delete is None:
            return
        if node_to_delete.is_root():
            if node_to_delete.is_leaf():
                self.root = None
                self.elements -= 1
            elif node_to_delete.has_both_children():
                max_node: TreeNode = node_to_delete.left.find_max()
                tmp_key = max_node.key
                tmp_value = max_node.value
                self.delete(tmp_key)
                node_to_delete.key = tmp_key
                node_to_delete.value = tmp_value
            else:
                if node_to_delete.has_left_child():
                    self.root = node_to_delete.left
                else:
                    self.root = node_to_delete.right
                self.root.parent = None
                self.elements -= 1
        else:
            if node_to_delete.is_leaf():
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left = None
                else:
                    node_to_delete.parent.right = None
                self.elements -= 1
            elif node_to_delete.has_both_children():
                max_node: TreeNode = node_to_delete.left.find_max()
                tmp_key = max_node.key
                tmp_value = max_node.value
                self.delete(tmp_key)
                node_to_delete.key = tmp_key
                node_to_delete.value = tmp_value
            elif node_to_delete.has_left_child():
                self.elements -= 1
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left = node_to_delete.left
                else:
                    node_to_delete.parent.right = node_to_delete.left
                node_to_delete.left.parent = node_to_delete.parent
            else:
                self.elements -= 1
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left = node_to_delete.right
                else:
                    node_to_delete.parent.right = node_to_delete.right
                node_to_delete.right.parent = node_to_delete.parent

    def find_min(self) -> TreeNode:
        if self.is_empty():
            return None
        node: TreeNode = self.root
        while node.left is not None:
            node = node.left
        return node

    def find_max(self) -> TreeNode:
        if self.is_empty():
            return None
        node: TreeNode = self.root
        while node.right is not None:
            node = node.right
        return node
