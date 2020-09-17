import pygame
from Path_Finder.Algorithms import a_star,Dijkstras, BFS
from Path_Finder.Visualization import make_grid,draw_grid, draw, mouse_position, reconstruct_path, generate_obstacle_map, screen
from Path_Finder.Square_class import Square


def main(screen, width):
    ROWS = 50
    grid = make_grid(ROWS,width)
    start = None
    end = None

    run = True
    started = False
    while run:
        draw(screen,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row,col = mouse_position(pos,ROWS,width)
                square1 = grid[row][col]
                if not start and square1!= end:
                    #print('setting_start')
                    start = square1
                    start.make_start()
                elif not end and square1!= start:
                    end = square1
                    end.make_end()
                elif square1 != end and square1 != start:
                    square1.make_obstacle()



            elif pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    row, col = mouse_position(pos, ROWS, width)
                    grid[row][col].reset()
                    if square1 == start:
                        start = None
                    elif square1 == end:
                        end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for square in row:
                            square.update_adjacent(grid)
                    pygame.display.set_caption("A* Path-Finding Algorithm")
                    a_star(lambda: draw(screen,grid,ROWS,width),grid,start,end)
                if event.key == pygame.K_d and start and end:
                    for row in grid:
                        for square in row:
                            square.update_adjacent(grid)
                    pygame.display.set_caption("Dijkstra's Path-Finding Algorithm")
                    Dijkstras(lambda: draw(screen,grid,ROWS,width),grid,start,end)
                if event.key == pygame.K_b and start and end:
                    for row in grid:
                        for square in row:
                            square.update_adjacent(grid)
                    pygame.display.set_caption("BFS Path-Finding Algorithm")
                    BFS(lambda: draw(screen,grid,ROWS,width),grid,start,end)
                if event.key == pygame.K_c:
                    pygame.display.set_caption("Path-Finder Visualization")
                    start = None
                    end = None
                    grid = make_grid(ROWS,width)

                if event.key == pygame.K_m:
                    pygame.display.set_caption("Path-Finder Visualization")
                    grid = make_grid(ROWS, width)
                    start,end = generate_obstacle_map(grid)



    pygame.quit()

main(screen, 800)

