import pygame


class Scoreboard:

    def __init__(self, screen_midtop):
        self.screen_midtop = screen_midtop
        self.font = pygame.font.SysFont(None, 32)
        self.color = (0, 26, 35)
        self.score = 0
        self.render_text()

    def render_text(self):
        self.text_surface = self.font.render(f"Score: {self.score}", True, self.color) 
        self.text_rect = self.text_surface.get_rect(midtop=self.screen_midtop)

    def increase_score(self):
        self.score += 1
        self.render_text()

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)

