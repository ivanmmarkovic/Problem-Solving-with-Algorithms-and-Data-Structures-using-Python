from union_find import UnionFind
from union_find import Node

uf: UnionFind = UnionFind()

uf.add_component('a')
uf.add_component('b')
uf.add_component('c')
uf.add_component('d')
uf.add_component('e')
uf.add_component('f')

print('Number of components', uf.number_of_components)

uf.unify('a', 'f')
uf.unify('b', 'c')
uf.unify('c', 'd')
uf.unify('d', 'e')

uf.unify('b', 'e')
uf.unify('a', 'c')

print('Number of components', uf.number_of_components)

for n in uf.components:
    node: Node = uf.components[n]
    print('node with key', node.key, 'has parent', node.root.key)
    print('node with key', node.key, 'has components', len(node.components_in_group))
