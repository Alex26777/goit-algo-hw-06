import networkx as nx

# Створення графа з вагами
G = nx.Graph()

# Додавання вершин (станцій)
станції = ["Станція 1", "Станція 2", "Станція 3", "Станція 4", "Станція 5"]
G.add_nodes_from(станції)

# Додавання ребер з вагами
G.add_edge("Станція 1", "Станція 2", weight=4)
G.add_edge("Станція 2", "Станція 3", weight=3)
G.add_edge("Станція 3", "Станція 4", weight=2)
G.add_edge("Станція 4", "Станція 5", weight=5)
G.add_edge("Станція 5", "Станція 1", weight=1)
G.add_edge("Станція 2", "Станція 4", weight=3)

# Використання алгоритму Дейкстри для знаходження найкоротшого шляху
# від "Станція 1" до всіх інших
paths = nx.single_source_dijkstra_path(G, "Станція 1")
path_lengths = nx.single_source_dijkstra_path_length(G, "Станція 1")

# Результати
print("Найкоротші шляхи від 'Станція 1' до інших станцій:")
for station, path in paths.items():
    print(f"{station}: {path}")

print("\nДовжини найкоротших шляхів від 'Станція 1' до інших станцій:")
for station, length in path_lengths.items():
    print(f"{station}: {length}")