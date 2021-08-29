from game import NQueen_Game
import pygame as pg
g = NQueen_Game()

def main():
    done = False
    while g.running:
        if g.curr_menu.run_display:
            g.curr_menu.display_menu()
          
    #if g.playing:
    g.game_loop()
    while not done:
	    for event in pg.event.get():
		    if event.type == pg.QUIT:
			    done = True  

main()