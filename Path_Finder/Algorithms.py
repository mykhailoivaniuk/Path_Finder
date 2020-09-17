import pygame
from math import sqrt
from queue import PriorityQueue
from queue import Queue
from Path_Finder.Visualization import reconstruct_path


def Dijkstras(draw,grid,start,end):
    count = 0
    dist = {spot: float('inf') for row in grid for spot in row}
    pred = {spot: None for row in grid for spot in row}
    dist[start] = 0
    done = set()
    to_do = PriorityQueue()
    to_do.put((0,count, start))
    while not to_do.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = to_do.get()[2]
        if current == end:
            reconstruct_path(pred,current,draw,start)
            end.make_end()
            start.make_start()
            return True
        if current not in done:
            done.add(current)
            for neighbor in current.adjacent:
                if dist[current] + 1 < dist[neighbor]:
                    count += 1
                    dist[neighbor] = dist[current] + 1
                    pred[neighbor] = current
                    to_do.put((dist[neighbor],count,neighbor))
                    neighbor.make_open_D()
        draw()
        if current != start:
            current.make_closed_D()
    return False

##Heuristics Function for A*
def dist(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    D1 = 1
    D2 = sqrt(2)
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    #return max(dx,dy) # diagonal distance for moving in 8 directions
    #return (dx+dy) + (D2-2)*min(dx,dy)
    return abs(x1-x2)+abs(y1-y2) # manhattan distance for moving in 4 directions
    #return D1 * sqrt(dx * dx + dy * dy)


def a_star(draw,grid, start,end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0,count,start))
    came_from = {}
    g_score = {spot: float('inf') for row in grid for spot in row} # current shortest distance to get from the start node to this node
    g_score[start] = 0
    f_score = {spot: float('inf') for row in grid for spot in row} # predicted distance from this node to the end node
    f_score[start] = dist(start.find_pos(), end.find_pos())

    open_set_hash = {start} # a set that helps us check if  something is in the Priority Queue

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from,end,draw,start)
            end.make_end()
            start.make_start()
            return True
            #make_path
        for neighbor in current.adjacent:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + dist(neighbor.find_pos(), end.find_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()

        if current != start:
            current.make_closed()
    return False

def BFS(draw,grid,start,end):
    pred = {spot: None for row in grid for spot in row}
    to_do = Queue()
    pred[start] = None
    to_do.put(start)
    while not to_do.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = to_do.get()
        for neighbor in current.adjacent:
            if pred[neighbor] == None:
                pred[neighbor] = current
                to_do.put(neighbor)
                neighbor.make_open_BFS()
        if current == end:
            reconstruct_path(pred,current,draw,start)
            end.make_end()
            start.make_start()
            return True
        draw()
        if current != start:
            current.make_closed_BFS()
    return False