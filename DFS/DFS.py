
## This the firts of a series of scripts, where I will learn and implement some
## of the most famous Search Algorithms.
## In order to really understand what I'm learning I will try to give a concrete implementation
## to these algorithms, and by concrete I mean that i will apply these algorithms to solve some 
## real cases or exercises
#
#
#
## This is the first script where I will use the Depth First Search algorithm, which is a 
## graph algorithm used to find a way to visit all the edges, in order to solve a Maze problem.
## Typically there are two ways to implement the DFS algorithm: Recurisvely or Iteratively
#

from pyamaze import maze, agent, COLOR
def DFS(m):
    '''
    Receives as input the map of the maze that you can generate directly from the file pyamaze
    and implement the dfs algorithm.Since the algorithm explores all the graph we want then only to return
    that path that can let us reach the goal. 
    We will always start from the bottom right of the maze and try to reach the upper left 
    '''

    start = (m.rows,m.cols)
    explored = [start]
    frontier = [start]
    path = {}
    
    while len(frontier)>0:
        # if we reach the goal, then we break the loop 
        curr = frontier.pop()
        if curr == (1,1):
            break
        for d in 'ESNW':
            # if the path in the current cell is open then i will the child cell
            if m.maze_map[curr][d] == True:
                if d == 'E':
                    child = (curr[0], curr[1]+1)
                if d == 'W':
                    child = (curr[0], curr[1]-1)
                if d == 'S':
                    child = (curr[0]+1, curr[1])
                if d == 'N':
                    child = (curr[0]-1, curr[1])
                if child not in explored:
                    explored.append(child)
                    frontier.append(child)
                    path[child] = curr

    fwd_path = {}
    cell = (1,1)
    while cell != start:
        fwd_path[path[cell]] = cell
        cell = path[cell]

    return fwd_path


                


# initialize the maze with fixed dimension
m = maze(50,50)
# generate the configuration of the maze randomly
m.CreateMaze() 
path = DFS(m)
agent = agent(m,footprints = True)
m.tracePath({agent:path})
# print(m.maze_map)
DFS(m)
m.run()
