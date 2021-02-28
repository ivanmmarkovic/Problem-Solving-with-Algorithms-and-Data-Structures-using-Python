
class Node:
    def __init__(self, key=None, root: 'Node' = None):
        self.key = key
        self.root: 'Node' = self
        self.components_in_group: dict = {}


class UnionFind:
    def __init__(self):
        self.components: dict = {}
        self.number_of_components: int = 0

    def add_component(self, key: str = None):
        self.components[key] = Node(key)
        self.number_of_components += 1

    def unify(self, a: str, b: str):

        if a not in self.components or b not in self.components:
            return

        node1: Node = self.components[a]
        node2: Node = self.components[b]

        if node1.root == node2.root:
            print(a, 'and', b, 'already in same group')
            return

        if len(node1.root.components_in_group) > len(node2.root.components_in_group):
            new_root: Node = node1.root
            old_root: Node = node2.root
            old_root.root = new_root
            for n in old_root.components_in_group:
                node: Node = old_root.components_in_group[n]
                node.root = new_root
                new_root.components_in_group[n] = node
            old_root.components_in_group = {}
            new_root.components_in_group[old_root.key] = old_root
        else:
            new_root: Node = node2.root
            old_root: Node = node1.root
            old_root.root = new_root
            for n in old_root.components_in_group:
                node: Node = old_root.components_in_group[n]
                node.root = new_root
                new_root.components_in_group[n] = node
            old_root.components_in_group = {}
            new_root.components_in_group[old_root.key] = old_root

        self.number_of_components -= 1

