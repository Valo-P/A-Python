# main.py
from models import *
from grid import *

"""
Main function
Genere une grille aleatoire et trouve le chemin le plus court
"""
def main():
    # Crée une grille , un point de départ et un point d'arrivée aléatoire
    # Prend en paramètre la taille de la grille
    grid, start, end = generate_random_grid(50, 50)

    # Convertie le point de départ et le point d'arrivée en noeuds
    start = Node(*start)
    print("Start X and Y")
    print(start.x, start.y)
    end = Node(*end)
    print("End X and Y")
    print(end.x, end.y)

    # Crée un graph à partir de la grille
    graph = Graph(grid)
    
    # plot_new_grid(grid, start, end)

    try:
        # Cherche le chemin le plus court
        path = shortest_path(graph, start, end)

        # Print le chemin trouvé
        print("Path found:")
        printed_nodes = set()
        for node in path:
            if (node.x, node.y) not in printed_nodes:
                print(f"({node.x}, {node.y})")
                if node.parent is not None:
                    print(f"Parent ({node.parent.x}, {node.parent.y})")
                printed_nodes.add((node.x, node.y))

        # Affiche la grille et le chemin trouvé
        print_grid(grid,path,start,end)

        # Genere un plot de la grille et du chemin trouvé
        plot_grid(grid, path, start, end)

    # Si aucun chemin n'est trouvé
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()