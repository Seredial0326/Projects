import turtle

"""
Las siguientes lineas de código son para setear la ventana de Turtle
"""
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Solver with Turtle")
wn.setup(width=800, height=800)
pixels = 300

"""
La siguiente lista "maze" crea el laberinto representado por caractares.

'#' representa las paredes y ' ' (espacio) representa el libre sendero
La 'S' represanta el origen de partida y la 'G' representa el final del recorrido
"""

# maze = [
#     "############",
#     "#S         #",
#     "########## #",
#     "#          #",
#     "# ##########",
#     "# #        #",
#     "# ######## #",
#     "#          #",
#     "# ##########",
#     "#          #",
#     "# ###### # #",
#     "#        # #",
#     "# ######## #",
#     "#G#        #",
#     "############"
# ]

maze = [
    "################################",
    "#S      #     #                #",
    "# ##### # # # # #### ######### #",
    "#   #   # #   #    # # #     # #",
    "# ### ### # # # ## ### # ### # #",
    "#   #   # # # ###  #     #     #",
    "### ### # # # #   ## ##### ### #",
    "#   #   # # # # ###  #     #   #",
    "# ##### # # # # #   ## ##### ###",
    "# #     # # #   # ###  #     # #",
    "# # ##### # # ###     ## ##### #",
    "# #     # #   # # ### ## # # # #",
    "# ##### # ### #   # # #  # # # #",
    "# #   # #   ####### # ##       #",
    "#   ### # #   #G       # #######",
    "# # #   # ### ##########       #",
    "### ## ##     #   #    ### ### #",
    "#    #    ##### # # ##   #     #",
    "# #########   ###   #### ## ####",
    "#           ### ### #### ## ####",
    "# ###### ##   # ###   #        #",
    "# #    #  ### #   # # ##########",
    "#   ## ##  ## # # # #          #",
    "# ####  ##    # # ############ #",
    "# #   #  #### # # #            #",
    "# # # ## #### # # ### ##########",
    "# # #  #    # # # #            #",
    "# # ## #### # # # ############ #",
    "# #             #              #",
    "################################"
]


"""
Lo siguiente crea la clase que permite dibujar el laberinto
"""

class MazeTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
    
    def change_color(self, coordinate_type):
        if coordinate_type == "start_point":
            self.color("green")
        elif coordinate_type == "end_point":
            self.color("yellow")
        elif coordinate_type == "default":
            self.color("black")
        

"""
Lo siguiente crea la clase que permite utilizar a la tortuga como un objeto
"""
class SolverTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.speed(1)


"""
El siguiente métod dibuja el laberinto
"""
def draw_maze(maze):
    start_pos, end_pos = None, None
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '#':
                maze_turtle.goto(x * 20 - pixels, pixels - y * 20)
                maze_turtle.stamp()
            elif maze[y][x] == 'S':
                start_pos = (x, y)
                maze_turtle.change_color("start_point")
                maze_turtle.goto(x * 20 - pixels, pixels - y * 20)
                maze_turtle.stamp()
                maze_turtle.change_color("default")
            elif maze[y][x] == 'G':
                end_pos = (x, y)
                maze_turtle.change_color("end_point")
                maze_turtle.goto(x * 20 - pixels, pixels - y * 20)
                maze_turtle.stamp()
                maze_turtle.change_color("default")
    return start_pos, end_pos


"""
El siguiente método  sirve como instrucción para mover a la tortuga a la 
siguiente casilla deseada del laberinto
"""
def move_turtle(x, y):
    solver_turtle.goto(x * 20 - pixels, pixels - y * 20)


"""
El siguiente método es el que corresponde a trabajar por parte de los alumnos.
Es el método encargado de resolver el laberinto.

Tiene 3 argumentos de entrada: El mapa del laberinto, la posición inicial y
la posición de destino.

Los métodos deben regresar ("return <valor / valores>") todos los posibles 
caminos especificando el más corto tanto vía Greedy como Backtracking.
"""

def is_safe(x, y, dx, dy, maze, visited):
    nx, ny = x + dx, y + dy
    if (maze[ny][nx] == " " or maze[ny][nx] == "G") and (nx, ny) not in visited:
        return True
    return False

def way_back(path, intersecciones, visited, parent):
    x, y = path[-1]
    solver_turtle.pensize(2)
    solver_turtle.pencolor("grey")
        
    if len(intersecciones) == 0:
        return path, visited, []
    
    while path[-1] != intersecciones[-1]:
        x, y = path[-1]
        girar(x,y,parent, 1)
        move_turtle(x, y)
        path.pop()
        visited.remove((x,y))
    
    x, y = path[-1]
    move_turtle(x, y)
    girar(x,y,parent, 1)
    
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        if is_safe(x, y, dx, dy, maze, visited):
            return path, visited, intersecciones
        
    way_back(path, intersecciones, visited, parent)
    intersecciones.pop()
    
    return path, visited, intersecciones

def way_back_vis(path, start, parent):
    solver_turtle.pencolor("grey")
    if len(path) == 0:
        return
    
    i = len(path) - 1
    while path[-1] != start:
            x, y = path[-1]
            girar(x,y,parent, 1)
            move_turtle(x, y)
            path.pop()
            i -= 1
    
    for i in range(len(path) - 1, -1, -1):
        if path[-1] != start:
            x, y = path[-1]
            girar(x,y,parent, 1)
            move_turtle(x, y)
            path.pop()
        else:
            x, y = path[-1]
            move_turtle(x, y)
            girar(x,y,parent, 1)
            break

def girar(x,y, parent, valor):
    mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    if valor == 0:
        giros = [270, 0, 90, 180]
    else:
        giros = [90, 180, 270, 0]
    
    if parent[(x,y)] != None:
        x_now, y_now = parent[(x, y)]
    
        now = (x - x_now, y - y_now)
    else:
        return
    
    for i in range(len(mov)):
        if mov[i] == now:
            indice = i
            break
        
    solver_turtle.seth(giros[indice])


def solve_maze_greedy(maze, start, end):
    solver_turtle.speed(0)

    x, y = start
    end_x, end_y = end
    stack = [(0, x, y)]
    visited = set()
    path = []
    intersecciones = []
    mejor_dist = [float("inf")]
    best_path = []
    parent = {start: None}
    all_paths = []
    
    while stack:
        dist, x, y = stack.pop()

        if (x, y) in visited:
            continue
        
        if x != start[0] and y != start[1]:
            solver_turtle.pendown()
            solver_turtle.pensize(2)
            solver_turtle.pencolor("blue")
            girar(x,y,parent, 0)
        visited.add((x, y))
        path.append((x,y))
        move_turtle(x, y)

        if (x, y) == (end_x, end_y):
            if len(path) <= mejor_dist[0]:
                mejor_dist[0] = len(path)
                best_path = path[:]
            if path not in all_paths:
                all_paths.append(path[:])
            path, visited, intersecciones = way_back(path, intersecciones, visited, parent)
            solver_turtle.pensize(2)
            solver_turtle.pencolor("blue")
            if len(intersecciones) > 1:
                intersecciones.pop()
            continue

        ways = len(stack)
        yes = False

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if is_safe(x, y, dx, dy, maze, visited):
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited:
                    yes = True
                    parent[(nx, ny)] = (x, y)
                    stack.append((dist+1, nx,ny))
        
        if yes == False:
            path, visited, intersecciones = way_back(path, intersecciones, visited, parent)
            solver_turtle.pensize(2)
            solver_turtle.pencolor("blue")
            if len(intersecciones) > 1:
                intersecciones.pop()
        
        if len(stack) - ways >= 2:
            intersecciones.append((x,y))
            
            
    way_back_vis(path, start, parent)
    all_paths.sort()
    return all_paths[:], best_path[:], mejor_dist[0]

def solve_maze_backtracking(maze, x, y, path, best_path, paths, end, visited, dist, parent):
    end_x, end_y = end

    if (x, y) in visited:
        return
    
    if x != 1 and y != 1:
        solver_turtle.pendown()
        solver_turtle.pensize(2)
        girar(x, y, parent, 0)
    
    solver_turtle.pencolor("dark orange")
    visited.add((x, y))
    move_turtle(x, y)

    if (x, y) == (end_x, end_y):
        if dist < best_path[1]:
            best_path[0] = path[:]
            best_path[1] = dist
        paths.append(path[:])
        visited.remove((x, y))
        visited = set()
        return

    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        if is_safe(x, y, dx, dy, maze, visited):
            nx, ny = x + dx, y + dy
            path.append((nx, ny))
            parent[(nx,ny)] = (x,y)
            solve_maze_backtracking(maze, nx, ny, path, best_path, paths, end, visited, dist + 1, parent)
            solver_turtle.pencolor("grey")
            move_turtle(x,y)
            girar(x, y, parent, 1)
            path.pop()
            
    visited.remove((x,y))
            

if __name__ == "__main__":
    maze_turtle = MazeTurtle()
    solver_turtle = SolverTurtle()
    
    start_pos, end_pos = draw_maze(maze)
    
    all_paths, best_path, dist = solve_maze_greedy(maze, start_pos, end_pos)
    print("greedy")
    print(f"Todos los caminos encontrados son: {all_paths}")
    print(f"El mejor camino es: {best_path} y la distancia que se recorrió para llegar al destino es {dist}")
    print()
    
    visited = set()
    best_path = [[], float('inf')]
    paths = []
    x,y = start_pos
    path = [(x,y)]
    parent = {start_pos : None}
    
    solver_turtle.speed(0.5)
    
    solve_maze_backtracking(maze, start_pos[0], start_pos[1], path, best_path, paths, end_pos, visited, 1, parent)
    paths.sort()
    print("Backtracking")
    print(f"Best path : {best_path[0]} recorres la distancia de {best_path[1]}")
    print(f"All paths: {paths}")
    
    wn.mainloop()
