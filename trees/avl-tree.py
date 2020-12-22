class TreeNode:
    def __init__(self, key=None, value=None, parent=None, left=None, right=None,
                 left_subtree_height: int = 0, right_subtree_height: int = 0, balance_factor: int = 0):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.left_subtree_height: int = left_subtree_height
        self.right_subtree_height: int = right_subtree_height
        self.balance_factor : int = balance_factor

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
        return self.parent.left == self

    def is_right_child(self) -> bool:
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


class AVLTree:
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
                self._update_balance_factor(root)
        else:
            if root.has_right_child():
                self._put(root.right, key, value)
            else:
                root.right = TreeNode(key, value, root)
                self.elements += 1
                self._update_balance_factor(root)

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
            return None
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
                # keep pointer to that node, not root, root might change
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
            parent: TreeNode = None
            if node_to_delete.is_leaf():
                parent = node_to_delete.parent
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
                parent = node_to_delete.parent
                self.elements -= 1
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left = node_to_delete.left
                else:
                    node_to_delete.parent.right = node_to_delete.left
                node_to_delete.left.parent = node_to_delete.parent
            else:
                parent = node_to_delete.parent
                self.elements -= 1
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left = node_to_delete.right
                else:
                    node_to_delete.parent.right = node_to_delete.right
                node_to_delete.right.parent = node_to_delete.parent
            if parent is not None:
                self._update_balance_factor(parent)

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

    def _update_balance_factor(self, root: TreeNode):
        old_balance_factor: int = root.balance_factor
        if root.has_left_child():
            root.left_subtree_height = max(root.left.left_subtree_height, root.left.right_subtree_height) + 1
        else:
            root.left_subtree_height = 0
        if root.has_right_child():
            root.right_subtree_height = max(root.right.left_subtree_height, root.right.right_subtree_height) + 1
        else:
            root.right_subtree_height = 0
        root.balance_factor = root.left_subtree_height - root.right_subtree_height
        if root.balance_factor < -1 or root.balance_factor > 1:
            self._rebalance(root)
            return
        if root.balance_factor != old_balance_factor and root.has_parent():
            self._update(root.parent)

    def _rebalance(self, root: TreeNode):
        if root.balance_factor < 0:
            if root.right.balance_factor > 0:
                self._rotate_right(root.right)
            else:
                self._rotate_left(root)
        else:
            if root.left.balance_factor < 0:
                self._rotate_left(root.left)
            else:
                self._rotate_right(root)

    def _rotate_left(self, root: TreeNode):
        old_root: TreeNode = root
        new_root: TreeNode = old_root.right
        old_root.right = new_root.left
        if new_root.has_left_child():
            new_root.left.parent = old_root
        new_root.parent = old_root.parent
        if old_root.has_parent():
            if old_root.is_left_child():
                old_root.parent.left = new_root
            else:
                old_root.parent.right = new_root
        else:
            self.root = new_root
        old_root.parent = new_root
        new_root.left = old_root
        self._update_balance_factor(old_root)

    def _rotate_right(self, root: TreeNode):
        old_root: TreeNode = root
        new_root: TreeNode = old_root.left
        old_root.left = new_root.right
        if new_root.has_right_child():
            new_root.right.parent = old_root
        new_root.parent = old_root.parent
        if old_root.has_parent():
            if old_root.is_left_child():
                old_root.parent.left = new_root
            else:
                old_root.parent.right = new_root
        else:
            self.root = new_root
        old_root.parent = new_root
        new_root.right = old_root
        self._update_balance_factor(old_root)



