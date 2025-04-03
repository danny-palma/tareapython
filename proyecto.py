import pygraphviz as pgv

def main():
  # Ingresar los nodos separados por coma
  entrada = input("Ingrese los nodos separados por coma (Ej: Gina, Paola, Genesis, Omar, Adis): ")
  nodos = [nodo.strip() for nodo in entrada.split(",") if nodo.strip()]

  # Ingresar el nodo a buscar
  objetivo = input("Ingrese el nodo a buscar: ").strip()

  ruta = []
  encontrado = False

  # Búsqueda secuencial de nodo
  for nodo in nodos:
    ruta.append(nodo)
    if nodo.lower() == objetivo.lower():
      encontrado = True
      break

  # Crear un grafo dirigido
  G = pgv.AGraph(strict=False, directed=True)

  # Agregar cada nodo de la ruta y conectar secuencialmente
  anterior = None
  for nodo in ruta:
      G.add_node(nodo)
      if anterior is not None:
          G.add_edge(anterior, nodo)
      anterior = nodo

  # Realzar el nodo encontrado (si se encontró)
  if encontrado:
      nodo_objetivo = G.get_node(objetivo)
      nodo_objetivo.attr['color'] = 'red'
      nodo_objetivo.attr['style'] = 'filled'
      nodo_objetivo.attr['fillcolor'] = 'lightgray'

  # Generar la imagen usando el layout 'dot'
  G.layout(prog='dot')
  G.draw('ruta_busqueda.png')
  print("La ruta de búsqueda se ha guardado en 'ruta_busqueda.png'")
  

if __name__ == '__main__':
  main()