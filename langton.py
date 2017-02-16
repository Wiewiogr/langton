import ant

direction = [[1,0],[0,-1],[-1,0],[0,1]]


class Board(object):
    def __init__(self,numberOfAnts,size):
        self.ants = [ant.Ant(i+1,size) for i in range(numberOfAnts)]
        self.size = size
        self.board = [[0 for x in range(size[0])] for y in range(size[1])]

    def next(self):
        changedFields = []
        for x in self.ants:
            #if x.color != self.board[x.x][x.y]:
            if self.board[x.x][x.y] == 0:
                self.board[x.x][x.y] = x.color
                changedFields.append([x.x,x.y,x.color])
                x.direction = (x.direction+1)%4
                x.x = (x.x+direction[x.direction][0])
                x.x %= self.size[0]
                x.y = (x.y+direction[x.direction][1])
                x.y %= self.size[1]
            else:
                self.board[x.x][x.y] = 0
                changedFields.append([x.x,x.y,0])
                x.direction = (x.direction-1)%4
                x.x = (x.x+direction[x.direction][0])%self.size[0]
                x.y = (x.y+direction[x.direction][1])%self.size[1]
        return changedFields




