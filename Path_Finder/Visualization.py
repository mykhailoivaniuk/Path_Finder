import random
import pygame
from Path_Finder.Square_class import Square, WHITE, GREY



WIDTH = 800
screen = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Path-Finder Visualization")

def make_grid(rows,width):
    grid = []
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            sq = Square(i,j,gap,rows)
            grid[i].append(sq)
    return grid


def draw_grid(win,rows,width):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(screen, GREY, (0,i*gap),(width,i*gap))
    for j in range(rows):
        pygame.draw.line(screen, GREY, (j*gap,0), (j*gap, width))

def generate_obstacle_map(grid):
    start = None
    end = None
    path_nodes = [(random.randrange(0, 50), random.randrange(0, 50)) for i in range(2)]
    start = grid[random.randrange(0, 50)][random.randrange(0, 25)]
    start.make_start()
    end = grid[random.randrange(0, 50)][random.randrange(25, 50)]
    end.make_end()

    obstacle_map = [(random.randrange(0, 50), random.randrange(0, 50)) for i in range(1000)]
    for element in obstacle_map:
        square = grid[element[0]][element[1]]
        if square != start and square!= end:
            square.make_obstacle()
    return start,end




def draw(screen, grid,rows,width):
    screen.fill(WHITE)
    for row in grid:
        for square in row:
            square.draw(screen)
    draw_grid(screen,rows,width)
    pygame.display.update()

def mouse_position(pos,rows,width):
    gap = width//rows
    y,x = pos
    row = y//gap
    col = x//gap
    return row,col

def reconstruct_path(came_from, current, draw,start):
    while current in came_from and current != start :
        current = came_from[current]
        if current == None:
            return
        current.make_path()
        draw()
