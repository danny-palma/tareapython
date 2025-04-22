import pygraphviz as pgv

def dfs(tree, current, target, path, found_path):
    path.append(current)
    if current.lower() == target.lower():
        found_path.extend(path)
        return True
    for child in tree.get(current, []):
        if dfs(tree, child, target, path, found_path):
            return True
    path.pop()
    return False

def build_tree():
    raiz = input("Ingrese el nodo raíz: ").strip()
    relaciones = input("Ingrese las relaciones en formato padre->hijo separados por coma (Ej: A->B, A->C, B->D): ").strip()
    tree = {}
    for relacion in relaciones.split(","):
        relacion = relacion.strip()
        if '->' in relacion:
            padre, hijo = [x.strip() for x in relacion.split("->")]
            tree.setdefault(padre, []).append(hijo)
    return raiz, tree

def main():
    raiz, tree = build_tree()
    objetivo = input("Ingrese el nodo a buscar: ").strip()

    camino_encontrado = []
    if not dfs(tree, raiz, objetivo, [], camino_encontrado):
        print("Nodo no encontrado en el árbol.")

    G = pgv.AGraph(strict=False, directed=True)
    # Agregar nodos y relaciones del árbol
    for padre, hijos in tree.items():
        G.add_node(padre)
        for hijo in hijos:
            G.add_node(hijo)
            G.add_edge(padre, hijo)

    # Realzar el nodo objetivo (si se encontró en el camino de búsqueda)
    if camino_encontrado:
        nodo_objetivo = G.get_node(objetivo)
        nodo_objetivo.attr['color'] = 'red'
        nodo_objetivo.attr['style'] = 'filled'
        nodo_objetivo.attr['fillcolor'] = 'lightgray'

    G.layout(prog='dot')
    G.draw('ruta_busqueda.png')
    print("El árbol se ha guardado en 'ruta_busqueda.png'")

if __name__ == '__main__':
    main()