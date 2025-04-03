# Documentación del Proyecto: Búsqueda Secuencial de Nodos con PyGraphviz

## Descripción
Este proyecto es un programa en Python que realiza una búsqueda secuencial en una lista de nodos introducidos por el usuario. Durante la ejecución, se construye un grafo dirigido que representa la ruta de búsqueda. Si el nodo objetivo es encontrado, este se resalta en el grafo. El grafo se genera usando la librería `pygraphviz` y se guarda como una imagen (`ruta_busqueda.png`).

## Funcionamiento Interno del Código
Internamente, el programa sigue estos pasos:
1. **Entrada y Procesamiento:**  
  El usuario ingresa una cadena de texto con los nodos, separados por comas. El programa limpia la entrada, eliminando espacios adicionales y convierte todos los nodos a un formato uniforme (por ejemplo, minúsculas) para garantizar una búsqueda case-insensitive.

2. **Búsqueda Secuencial:**  
  Se recorre la lista de nodos uno a uno. Durante este recorrido, se va construyendo un grafo dirigido. Cada nodo se añade como vértice del grafo y se conecta con el nodo siguiente mediante una flecha que indica el orden de búsqueda. Cuando encuentra el nodo que coincide con el criterio de búsqueda, se marca visualmente (por ejemplo, cambiando su color o forma).

3. **Generación del Grafo:**  
  Utilizando `pygraphviz`, el programa crea el grafo en memoria. Se utiliza el motor de layout `dot` para organizar los nodos de manera jerárquica. Finalmente, se genera una imagen (`ruta_busqueda.png`) que muestra cómo se realizó la búsqueda, resaltando el nodo encontrado si existe.

4. **Salida:**  
  El usuario recibe la imagen generada y, opcionalmente, mensajes en consola que indican si el nodo fue encontrado o no.

## Requisitos
- Python 3.x
- [Graphviz](https://graphviz.org/) (instalado en el sistema)
- La librería de Python [pygraphviz](https://pygraphviz.github.io/)

## Clonando el Repositorio
Para clonar el repositorio, ejecuta en tu terminal:
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio/tareapython
```
*Nota: Reemplaza `tu_usuario` y `tu_repositorio` por los nombres correspondientes.*

## Instalación
1. Instala Graphviz en tu sistema. En sistemas basados en Debian/Ubuntu, puedes usar:
  ```bash
  sudo apt-get install graphviz
  ```
  En Windows, descarga e instala Graphviz desde [aquí](https://graphviz.org/download/).

2. Instala la librería `pygraphviz` mediante pip:
  ```bash
  pip install pygraphviz
  ```

## Cómo Ejecutar el Código
1. Abre una terminal en el directorio `g:/danie/repos/tareapython`.
2. Ejecuta el programa:
  ```bash
  python proyecto.py
  ```
3. Sigue las instrucciones:
  - Introduce los nodos separados por coma (por ejemplo, `hierro, bronce, slime, diamante, lapislázuli`).
  - Introduce el nodo a buscar.

El programa generará la imagen `ruta_busqueda.png` con la ruta de búsqueda y, si el nodo es encontrado, este se resaltará visualmente.

## Ejemplo de Uso

### Ejemplo 1: Buscar un material existente
- **Entrada:**
  ```
  Ingrese los nodos separados por coma (Ej: hierro, bronce, slime, diamante, lapislázuli): hierro, bronce, slime, diamante, lapislázuli
  Ingrese el nodo a buscar: slime
  ```
- **Resultado:**
  Se resalta el nodo `slime` en la ruta y se genera el archivo `ruta_busqueda.png`.

### Ejemplo 2: Buscar un material que no existe en la lista
- **Entrada:**
  ```
  Ingrese los nodos separados por coma (Ej: hierro, bronce, slime, diamante, lapislázuli): hierro, bronce, slime, diamante, lapislázuli
  Ingrese el nodo a buscar: oro
  ```
- **Resultado:**
  El programa recorre la lista completa y crea el grafo con todos los nodos de la ruta sin resaltar ningún nodo en particular, generando el archivo `ruta_busqueda.png`.

## Notas Adicionales
- El programa elimina espacios extra al procesar la lista de nodos.
- La búsqueda es insensible a mayúsculas y minúsculas.
- La imagen generada utiliza `dot` como motor de layout, adecuado para grafos dirigidos.

## Contribución
Si deseas contribuir al proyecto:
1. Haz un fork del repositorio.
2. Crea una rama para tu nueva característica o corrección.
3. Realiza los cambios y envía un pull request.

## Licencia
Este proyecto se puede distribuir y modificar según los términos de la licencia aplicable.
