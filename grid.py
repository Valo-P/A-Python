import matplotlib.pyplot as plt
import numpy as np

"""
Création d'une grille , d'un point de départ et d'un point d'arrivée aléatoire
"""
def generate_random_grid(rows, cols, p=0.3):
    # Genere une grille vide
    grid = np.zeros((rows, cols))

    # Randomise le point de départ et le point d'arrivée
    start = (np.random.randint(rows), np.random.randint(cols))
    end = (np.random.randint(rows), np.random.randint(cols))
    while start == end:
        end = (np.random.randint(rows), np.random.randint(cols))

    # Randomise les obstacles
    for i in range(rows):
        for j in range(cols):
            if (i, j) != start and (i, j) != end and np.random.rand() < p:
                grid[i][j] = 1

    return grid.astype(int), start, end

"""
Affiche la grille et le chemin trouvé dans la console
"""
def print_grid(grid, path, start, end):
    # Convertie le chemin en un ensemble de coordonnées pour une recherche plus rapide
    path_coords = set((node.x, node.y) for node in path)

    # Affiche la grille
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) in path_coords:
                # Si cette cellule est le débu
                if (i, j) == (start.x, start.y):
                    print('S', end=' ')
                # Si cette cellule est la fin
                elif (i, j) == (end.x, end.y):
                    print('E', end=' ')
                # Si cette cellule est sur le chemin
                else:
                    print('*', end=' ')
            else:
                # Si cette cellule n'est pas sur le chemin
                print(int(cell), end=' ')

        print() # Nouvelle ligne

"""
Affiche la grille et le chemin trouvé dans un plot
"""
def plot_grid(grid, path):

    # Genere une nouvelle figure et un axe
    fig, ax = plt.subplots()

    # Display la grille en image
    ax.imshow(grid, cmap='binary')

    # Plot le path
    if path is not None:
        path_x = [node.x for node in path]
        path_y = [node.y for node in path]
        ax.plot(path_y, path_x, color='red')

    # Montre le plot
    plt.show()