import pygame

class Square:
    def __init__(self, row, col, width, total_rows):
        self.total_rows = total_rows
        self.col = col
        self.row = row
        self.x = width * row
        self.y = width * col
        self.adjacent = []
        self.width = width
        self.color = WHITE

    def find_pos(self):
        return self.row,self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_obstacle(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == WHITE

    def is_finish(self):
        return self.color == PURPLE

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = LIGHT_BLUE

    def make_open(self):
        self.color = CORAL

    def make_closed_D(self):
        self.color = GREEN

    def make_open_D(self):
        self.color = YELLOW

    def make_open_BFS(self):
        self.color = YELLOW

    def make_closed_BFS(self):
        self.color = DARK_GREEN

    def make_obstacle(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = BLUE

    def make_path(self):
        self.color = PURPLE

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.width))

    def update_adjacent(self,grid):
        self.adjacent = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_obstacle(): #Above
            self.adjacent.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle(): #Below
            self.adjacent.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_obstacle(): #Right
            self.adjacent.append(grid[self.row][self.col+1])

        if self.col > 0 and not grid[self.row][self.col -1 ].is_obstacle(): #Left
            self.adjacent.append(grid[self.row ][self.col - 1 ])


    def __lt__(self, other):
        return False

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (128,0,128)
BLACK = (0,0,0)
GREY = (128,128,128)
WHITE = (255,255,255)
DARK_GREEN= (0,100,0)
ORANGE = (255,140,0)
LIGHT_BLUE = (173,216,230)
CORAL = (240,128,128)
YELLOW = (255,255,0)