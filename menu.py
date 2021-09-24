import pygame as pg

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w = self.game.DISPLAY_W/2
        self.mid_h = self.game.DISPLAY_H/2
        self.run_display = True
        self.cursor_rect = pg.Rect(0, 0, 20, 20)
        self.offset = -100
    
    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pg.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx = self.mid_w
        self.starty = self.mid_h + 30
        '''self.optionsx = self.mid_w
        self.optionsy = self.mid_h + 50'''
        self.creditsx = self.mid_w
        self.creditsy = self.mid_h + 50
        self.cursor_rect.midtop = (self.startx+self.offset+50, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("N-QUEENS", 40, self.mid_w, self.mid_h - 20)
            self.game.draw_text("Start Game", 15, self.startx, self.starty)
            #self.game.draw_text("Options", 15, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 15, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()
        
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.creditsx+self.offset+65, self.creditsy)
                self.state = "Credits"
                '''elif self.state == "Options":
                self.cursor_rect.midtop = (self.creditsx+self.offset+50, self.creditsy)
                self.state = "Credits"'''
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.startx+self.offset+50, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.creditsx+self.offset+65, self.creditsy)
                self.state = "Credits"
                '''elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx+self.offset+50, self.starty)
                self.state = "Start"'''
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.startx+self.offset+50, self.starty)
                self.state = "Start"
    
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.curr_menu = self.game.player_type
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False
        
'''class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Volume"
        self.volx = self.mid_w
        self.voly = self.mid_h + 20
        self.controlsx = self.mid_w
        self.controlsy = self.mid_h+40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Options", 20, self.mid_w, self.mid_h - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            pass'''

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('CREDITS:', 20, self.mid_w, self.mid_h - 60)
            self.game.draw_text('(In alphabetical order)', 10, self.mid_w, self.mid_h - 40)
            self.game.draw_text('Debashish Majumdar', 15, self.mid_w, self.mid_h - 10)
            self.game.draw_text('Manika Battan', 15, self.mid_w, self.mid_h + 10)
            self.game.draw_text('Sameeksha Sharma', 15, self.mid_w, self.mid_h + 30)
            self.game.draw_text('Vibhu Gupta', 15, self.mid_w, self.mid_h + 50)
            self.blit_screen()

class PlayerTypeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "AI"
        self.aix = self.mid_w
        self.aiy = self.mid_h + 20
        self.humanx = self.mid_w
        self.humany = self.mid_h+40
        self.cursor_rect.midtop = (self.aix + self.offset + 85, self.aiy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Choose Player Type:", 20, self.mid_w, self.mid_h - 30)
            self.game.draw_text("AI", 15, self.aix, self.aiy)
            self.game.draw_text("HUMAN", 15, self.humanx, self.humany)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.game.reset_player_type_values()
            self.run_display = False
        elif self.game.START_KEY:
            self.game.curr_menu = self.game.board_size
            if self.state == 'AI':
                self.game.AI = True
            elif self.state == 'HUMAN':
                self.game.HUMAN = True
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'AI':
                self.state = 'HUMAN'
                self.cursor_rect.midtop = (self.humanx + self.offset + 65, self.humany)
            elif self.state == 'HUMAN':
                self.state = 'AI'
                self.cursor_rect.midtop = (self.aix + self.offset + 85, self.aiy)

class BoardSizeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "sizefour"
        self.fourx = self.mid_w
        self.foury = self.mid_h + 30
        self.sixx = self.mid_w
        self.sixy = self.mid_h + 50
        self.eightx = self.mid_w
        self.eighty = self.mid_h + 70
        self.cursor_rect.midtop = (self.fourx + self.offset+80, self.foury)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Choose Board Size:", 20, self.mid_w, self.mid_h - 20)
            self.game.draw_text("4x4", 15, self.fourx, self.foury)
            self.game.draw_text("6x6", 15, self.sixx, self.sixy)
            self.game.draw_text("8x8", 15, self.eightx, self.eighty)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.player_type
            self.game.reset_player_type_values()
            self.run_display = False
        elif self.game.START_KEY:
            if self.state == "sizefour":
                self.game.board_four = True   
            elif self.state == "sizesix":
                self.game.board_six = True   
            elif self.state == "sizeeight":
                self.game.board_eight = True
            if self.game.AI:
                self.game.playing_AI = True
            elif self.game.HUMAN:
                self.game.playing_H = True
            self.game.running = False
            self.run_display = False
    
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "sizefour":
                self.cursor_rect.midtop = (self.sixx+self.offset+80, self.sixy)
                self.state = "sizesix"
            elif self.state == "sizesix":
                self.cursor_rect.midtop = (self.eightx+self.offset+80, self.eighty)
                self.state = "sizeeight"
            elif self.state == "sizeeight":
                self.cursor_rect.midtop = (self.fourx+self.offset+80, self.foury)
                self.state = "sizefour"
        elif self.game.UP_KEY:
            if self.state == "sizefour":
                self.cursor_rect.midtop = (self.eightx+self.offset+80, self.eighty)
                self.state = "sizeeight"
            elif self.state == "sizesix":
                self.cursor_rect.midtop = (self.fourx+self.offset+80, self.foury)
                self.state = "sizefour"
            elif self.state == "sizeeight":
                self.cursor_rect.midtop = (self.sixx+self.offset+80, self.sixy)
                self.state = "sizesix"
