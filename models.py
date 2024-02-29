from queue import PriorityQueue

"""
Noeud de la grille
"""
class Node:
    def __init__(self, x, y, cost=0, heuristic=0, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent
    
    def __lt__(self, other):
        return self.heuristic < other.heuristic

"""
Graph de la grille
"""
class Graph:
    def __init__(self, grid):
        self.grid = grid

    def get_neighbors(self, node):
        neighbors = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares
            node_position = (node.x + new_position[0], node.y + new_position[1])

            # Si c'est dans la plage
            if node_position[0] > (len(self.grid) - 1) or node_position[0] < 0 or node_position[1] > (len(self.grid[len(self.grid)-1]) -1) or node_position[1] < 0:
                continue

            # Si le terrain est praticable / pas un obstacle
            if self.grid[node_position[0]][node_position[1]] != 0:
                continue

            # Créez un nouveau nœud
            new_node = Node(node_position[0], node_position[1])
            neighbors.append(new_node)

        return neighbors

"""
Distance de Manhattan entre deux points
"""
def distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

"""
Algorithme de recherche de chemin / A*
"""
def shortest_path(graph, start, end):
    closed_list = []
    open_list = PriorityQueue()
    open_list.put((0, start))

    # Tant que la liste ouverte n'est pas vide
    while not open_list.empty():
        _, current_node = open_list.get()

        # Si le noeud actuel est le noeud de fin
        if current_node.x == end.x and current_node.y == end.y:
            closed_list.append(current_node)
            return reconstruct_path(closed_list)

        # Pour chaque voisin du noeud actuel
        for neighbor in graph.get_neighbors(current_node):
            # Si le voisin n'est pas dans la liste fermée ou s'il est dans la liste ouverte et a un coût inférieur
            if neighbor not in closed_list or any(neighbor == node and neighbor.cost < node.cost for _, node in open_list.queue):
                # Calculer le coût
                neighbor.cost = current_node.cost + 1
                # Calculer le coût heuristique
                neighbor.heuristic = neighbor.cost + distance(neighbor, end)
                # Mettre à jour le parent
                neighbor.parent = current_node
                # Ajouter le voisin à la liste ouverte
                open_list.put((neighbor.heuristic, neighbor))

        # Ajouter le noeud actuel à la liste fermée
        closed_list.append(current_node)

    # Si aucun chemin n'est trouvé
    raise Exception("No path found")


"""
Reconstruit le chemin à partir de la liste fermée
"""
def reconstruct_path(list):
    path = []
    # Remonte le chemin à partir du dernier noeud
    node = list[-1]

    # Tant que le noeud a un parent
    while node is not None:
        path.append(node)
        node = node.parent

    return path