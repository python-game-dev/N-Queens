import pygame as pg

class Board():
    def __init__(self, game):
        self.game = game
        self.board_display = False
        self.surface_size = 512
        self.board_surface = pg.Surface((self.surface_size, self.surface_size))
        self.square_size = 0 
        self.the_square = (0,0,0,0)
        self.colors = [self.game.WHITE, self.game.BLACK]
        #self.board_window = pg.display.set_mode((self.surface_size, self.surface_size))
        self.column_index = 0
    def draw_board(self, n):
        self.board_display = True
        while self.board_display:
            self.game.check_events()
            self.board_surface.fill(self.game.BLACK)
            self.square_size = self.surface_size//n
            self.surface_size = n*self.square_size
            self.board_window = pg.display.set_mode((self.surface_size, self.surface_size))
            for row in range(n):           
                self.c_indx = row % 2           
                for col in range(n):       
                    self.the_square = (col*self.square_size, row*self.square_size, self.square_size, self.square_size)
                    self.board_window.fill(self.colors[self.c_indx], self.the_square)
                    # Now flip the color index for the next square
                    self.c_indx = (self.c_indx + 1) % 2
                    
            pg.display.flip()
            #self.blit_screen()
    
    def blit_screen(self):
        self.surface.blit(self.board_surface, (0,0))
        pg.display.update()
        self.game.reset_keys()