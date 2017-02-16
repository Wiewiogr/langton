import sys, pygame, langton
pygame.init()

grid = 6
size = width, height = 1000,1000
black = 0, 0, 0
screen = pygame.display.set_mode(size)
gridSize = int(width/grid), int(height/grid)
field = pygame.Rect(3, 3, 3, 3)

board = langton.Board(9,gridSize)

colors = [[0,0,0],[0,100,200],[200,100,0],[100,200,0],[230,150,18],[255,0,0],[224,23,246],[23,231,246],[255,255,0],[160,160,0]]
i = 0
clock = pygame.time.Clock()
while 1:
    i += 1
    print i
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    #screen.fill(black)


    #for i in xrange(len(board.board)):
    #    for j in xrange(len(board.board[i])):
    #        if board.board[i][j] != 0:
    #            pygame.draw.rect(screen,colors[board.board[i][j]],pygame.Rect(i*grid,j*grid,grid,grid))
    #board.next()
    #pygame.display.flip()

    rects = []
    for x in board.next():
        rect = pygame.Rect(x[0]*grid,x[1]*grid,grid,grid)
        pygame.draw.rect(screen,colors[x[2]],rect)
        rects.append(rect)
    pygame.display.update(rects)
    clock.tick(240)
