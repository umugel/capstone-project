import random
import pygame
class button():
    def __init__(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.pos = pos
        self.width = width
        self.height = height
    def clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            return True
        return False
class RpsGam():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("Rps smasher")
        self.bg = pygame.image.load("background.jpg")
        self.r_btn =
pygame.image.load("r_button.png").convert_alpha()
        self.p_btn =
pygame.image.load("p_button.png").convert_alpha()
        self.s_btn =
pygame.image.load("s_button.png").convert_alpha()
        self.choose_rock =
pygame.image.load("rock.png").convert_alpha()
        self.choose_paper =
pygame.image.load("paper.png").convert_alpha()
        self.choose_scissor =
pygame.image.load("scissor.png").convert_alpha()
       self.screen.blit(self.bg, (0, 0))
       self.screen.blit(self.r_btn, (20, 500))
       self.screen.blit(self.p_btn, (330, 500))
       self.screen.blit(self.s_btn, (640, 500))
       self.rock_btn = button(30, 520, (30, 520), 300, 140)
       self.paper_btn = button(340, 520, (340, 520), 300, 140)
       self.scissor_btn = button(640, 520, (640, 520), 300, 140)
       self.font = pygame.font.Font("Splatch.ttf", 90)
       self.text = self.font.render(f"", True, (255, 255, 255))
       self.pl_score = 0
       self.pc_score = 0
    def player(self):
      if self.rock_btn.clicked(30):
            self.p_option = "rock"
            self.screen.blit(self.choose_rock, (120, 200))
      elif self.paper_btn.clicked(340):
            self.p_option = "paper"
            self.screen.blit(self.choose_paper, (120, 200))
      else:
            self.p_option = "scissor"
            self.screen.blit(self.choose_scissor, (120, 200))
      return
    def computer(self):
        self.pc_random = " "
        options = ["rock", "paper", "scissor"]
        pc_random = random.choice(list(options))
        if pc_choice == "rock":
            self.pc_random_choice = "rock"
        elif pc_choice == "paper":
            self.pc_random_choice = "paper"
            pc_choice = "paper"
        else:            
             self.pc_random_choice = "scissor"
             pc_choice = "scissor"
        pc_option = self.screen.blit(self.choose_rock, (600, 200))
        return pc_option
    def pl_score_cache(self):
      self.pl_score = 0
      self.pc_score = 0