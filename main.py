from game import NQueen_Game
import pygame as pg
import sys, random
import math

g = NQueen_Game()

class QueenSprite:
    def __init__(self, img, target_posn):
        self.image = img
        self.target_posn = target_posn
        self.posn = self.target_posn
        self.y_velocity = 0
        self.dragging = False
    
    def update(self):
        return

    def drag_with_mouse(self, mousex, mousey):
        if self.dragging:
            self.posn = (mousex, mousey)
        return None
    
    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)

    def mouse_touch_sprite(self, mousex, mousey):
        center_x = self.posn[0]
        center_y = self.posn[1]
        distance_mouse = math.sqrt((mousex - center_x)**2 + (mousey - center_y)**2)
        print('distance to mouse: ', distance_mouse)
        if distance_mouse < 40:
            return True
        else:
            return False

def share_diagonal(x0, y0, x1, y1):
    dy = y1-y0
    dx = x1-x0

    return abs(dx) == abs(dy)

def col_clashes(exist_chess, index):
    for i in range(index):
        if share_diagonal(i, exist_chess[i], index, exist_chess[index]):
            return True
    return False

def has_clashes_2(chess_list):
    for i, item in enumerate(chess_list):
        if item == -1:
            continue
    
        for j, pre_item in enumerate(chess_list):
            if j>= i:
                break

            if pre_item == -1:
                continue

            if share_diagonal(j, pre_item, i, item):
                return True

    return False

def draw_board_H(n):
    pg.init()
    colors = [(255,255,255),(0,0,0)]

    surface_sz = 512
    sq_sz = surface_sz//n
    surface_sz = n*sq_sz

    display_surface = pg.display.set_mode((surface_sz, surface_sz))
    pg.display.set_caption("N Queens")
        
    green_queen = pg.transform.scale(pg.image.load('images/green_queen.png'), (sq_sz, sq_sz))
    queen_offset = (sq_sz-green_queen.get_width())//2
    win_image = pg.image.load('images/banner.png')

    all_sprites = []
    chess_board = [-1]*n

    FPS = 30
    fpsClock = pg.time.Clock()

    is_win = False

    while True:
        for row in range(n):
            c_indx = row % 2
            for col in range(n):
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                display_surface.fill(colors[c_indx], the_square)
                c_indx = (c_indx + 1) % 2

        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif e.type == pg.MOUSEMOTION:
                mousex, mousey = e.pos
                
            elif e.type == pg.MOUSEBUTTONDOWN:
                if not is_win:
                    mousex, mousey = e.pos
                    col_index = mousex // sq_sz
                    row_index = mousey // sq_sz

                    for item in all_sprites:
                        if item.mouse_touch_sprite(mousex, mousey):
                            item.dragging = True
                            chess_board[row_index] = -1
                            break
                
            elif e.type == pg.MOUSEBUTTONUP:
                if not is_win:
                    mousex, mousey = e.pos
                    col_index = mousex //sq_sz
                    row_index = mousey //sq_sz

                    if chess_board[row_index]!=-1 or (col_index in chess_board):
                        print(chess_board)
                    else:
                        chess_board[row_index] = col_index
                        print(chess_board)
                        if has_clashes_2(chess_board):
                            chess_board[row_index] = -1
                            print(chess_board)
                        else:
                            drag_existing = False
                            for item in all_sprites:
                                if item.dragging:
                                    drag_existing = True
                                    item.dragging = False
                                    item.posn = (col_index*sq_sz, row_index*sq_sz)
                                    break 
                        
                            if not drag_existing:
                                if len(all_sprites) < n:
                                    a_queen = QueenSprite(green_queen, (col_index * sq_sz + queen_offset, row_index * sq_sz + queen_offset))
                                all_sprites.append(a_queen)

                            if -1 not in chess_board:
                                is_win = True

        for sprite in all_sprites:
            if sprite.dragging:
                sprite.drag_with_mouse(mousex, mousey)
            else:
                sprite.update()
        
            sprite.draw(display_surface)

        if is_win:
            display_surface.blit(win_image, (0,surface_sz/2-64))
    
        pg.display.update()
        fpsClock.tick(FPS)


def main():
    done = False
    pg.display.set_caption('N Queens')
    while g.running:
        g.curr_menu.display_menu()
        
    
    g.game_loop()


    while g.playing_H:
        if g.HUMAN and g.board_four:
            draw_board_H(4)
        if g.HUMAN and g.board_six:
            draw_board_H(6)
        if g.HUMAN and g.board_eight:
            draw_board_H(8)

    while not done:
	    for event in pg.event.get():
		    if event.type == pg.QUIT:
			    done = True

main()