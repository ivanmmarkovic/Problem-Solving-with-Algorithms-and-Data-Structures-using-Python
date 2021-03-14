from typing import List

def find_parent(i: int, components: List[int]) -> int:
    
    while i != components[i]:
        i = components[i]
    return i


class Graph:
    def number_of_connected_components(self, edges_matrix: List[List[int]]) -> int:
        
        n: int = len(edges_matrix)
            
        number_of_components: int = n
            
        components: List[int] = [None] * n
            
        for i in range(n):
            components[i] = i
            
        for i in range(n):
            
            for j in range(n):
                
                if edges_matrix[i][j] == 1:
                    
                    parent_one: int = find_parent(i, components)
                    parent_two: int = find_parent(j, components)
                        
                    if parent_one != parent_two:
                        components[parent_one] = parent_two
                        number_of_components -= 1
                        
        return number_of_components