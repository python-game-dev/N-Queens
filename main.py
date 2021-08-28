from game import NQueen_Game

g = NQueen_Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()