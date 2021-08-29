import pygame as pg
#from solution import *
import time
class Board():
    def __init__(self, game):
        self.game = game
        #self.board_display = False
        self.surface_size = 512
        self.board_surface = pg.Surface((self.surface_size, self.surface_size))
        self.square_size = 0 
        self.the_square = (0,0,0,0)
        self.colors = [self.game.WHITE, self.game.BLACK]
        #self.board_window = pg.display.set_mode((self.surface_size, self.surface_size))
        self.column_index = 0
        self.posArray = []

    def draw_board(self, n):
        self.game.check_events()
        self.board_surface.fill(self.game.BLACK)
        self.square_size = self.surface_size//n
        self.surface_size = n*self.square_size
        self.board_window = pg.display.set_mode((self.surface_size, self.surface_size))
        for row in range(n):
            self.tempPos = []           
            self.c_indx = row % 2           
            for col in range(n):
                self.tempPos.append((col*self.square_size, row*self.square_size))       
                self.the_square = (col*self.square_size, row*self.square_size, self.square_size, self.square_size)
                self.board_window.fill(self.colors[self.c_indx], self.the_square)
                # Now flip the color index for the next square
                self.c_indx = (self.c_indx + 1) % 2
            self.posArray.append(self.tempPos)
        
        self.soln = self.soln([], n)
        self.draw_soln(self.board_window, self.soln, self.posArray, self.square_size)

        #pg.display.flip()
        pg.display.update()

        for row in range(n):
            for col in range(n):
                print(self.posArray[row][col], end=" ")
            print()
        #self.blit_screen()

    def draw_soln(self, window, soln, array, size):
        self.img= [pg.transform.scale(pg.image.load('images/black_queen.png'), (size,size))]
        self.img.append(pg.transform.scale(pg.image.load('images/white_queen.png'), (size,size)))
        self.col = 0
        print(soln)
        for i in (soln):
            time.sleep(0.7)
            self.x, self.y = array[self.col][i]
            window.blit(self.img[(i+self.col)%2], (self.x, self.y))
            self.col+=1
            pg.display.update()
    
    #Main driver and solution code
    def soln(self, arr, n, ans=False):
        if(len(arr)==n):
            return arr
        for i in range(n):
            if i not in arr:
                arr.append(i)
                if(self.place(arr)):
                    ans = self.soln(arr,n)
                    if(ans):
                        return ans
                arr.pop()
        return ans

    def place(self, arr):
        i=len(arr)-1
        for j in range(i):
            if( i-j == abs(arr[i]-arr[j])):
                return False
        return True
       
    def blit_screen(self):
        self.surface.blit(self.board_surface, (0,0))
        pg.display.update()
        self.game.reset_keys()