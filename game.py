import pygame
from menu import *
from board import *
class NQueen_Game():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.AI = False
        self.HUMAN = False
        self.board_four = False
        self.board_six = False
        self.board_eight = False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.DISPLAY_W = 480
        self.DISPLAY_H = 270
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = 'Retro Gaming.ttf'
        self.BLACK = (0,0,0)
        self.WHITE = (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.player_type = PlayerTypeMenu(self)
        self.board_size = BoardSizeMenu(self)
        #self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.board = Board(self)
    def game_loop(self):
        self.playing = True
        if self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing=False
            self.display.fill(self.BLACK)
            if self.AI and self.board_four:
                #self.draw_text('Type: AI', 20, self.DISPLAY_W/2, self.DISPLAY_H/2-20)
                #self.draw_text('Size: 4', 20, self.DISPLAY_W/2, self.DISPLAY_H/2 + 10)
                self.board.draw_board(4)
                
            elif self.AI and self.board_six:
                #self.draw_text('Type: AI', 20, self.DISPLAY_W/2, self.DISPLAY_H/2-20)
                #self.draw_text('Size: 6', 20, self.DISPLAY_W/2, self.DISPLAY_H/2 + 10)
                self.board.draw_board(6)
                
            elif self.AI and self.board_eight:
                #self.draw_text('Type: AI', 20, self.DISPLAY_W/2, self.DISPLAY_H/2-20)
                #self.draw_text('Size: 8', 20, self.DISPLAY_W/2, self.DISPLAY_H/2 + 10)
                self.board.draw_board(8)
                 
            elif self.HUMAN and self.board_four:
                #self.draw_text('Type: HUMAN', 20, self.DISPLAY_W/2, self.DISPLAY_H/2-20)
                #self.draw_text('Size: 4', 20, self.DISPLAY_W/2, self.DISPLAY_H/2 + 10)
                self.board.draw_board(4)
            elif self.HUMAN and self.board_six:
                #self.draw_text('Type: HUMAN', 20, self.DISPLAY_W/2, self.DISPLAY_H/2-20)
                #self.draw_text('Size: 6', 20, self.DISPLAY_W/2, self.DISPLAY_H/2 + 10)
                self.board.draw_board(6)
            elif self.HUMAN and self.board_eight:
                #self.draw_text('Type: HUMAN', 20, self.DISPLAY_W/2, self.DISPLAY_H/2-20)
                #self.draw_text('Size: 8', 20, self.DISPLAY_W/2, self.DISPLAY_H/2 + 10)
                self.board.draw_board(8)
            #self.board.board_window.blit(self.board.board_surface, (0,0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                self.curr_menu.run_display = False
                self.AI = False
                self.HUMAN = False
                self.boardFour = False
                self.boardSix = False
                self.boardEight = False
                self.board.board_display = False
                self.board.tempPos =[]
                self.board.posArray = []
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

    def reset_player_type_values(self):
        self.AI = False
        self.HUMAN = False

    def reset_board_size_values(self):
        self.board_four = False
        self.board_six = False
        self.board_eight = False
    
    def reset_keys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
    

        

