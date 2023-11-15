import pygame

from app.config import *
from app.arraystate.algorithmstep import AlgorithmStepper


class SortingAnimation:
    def __init__(self, ARRAY, ALG_INDEX):
        pygame.init()

        self.iteration = 0
        self.running = True

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, TXT_SIZE)

        self.algorithm_state = AlgorithmStepper(self, ARRAY, ALG_INDEX)

    def draw(self):
        self.screen.fill(WHITE)
        self.algorithm_state.draw()

    def update(self):
        pygame.display.set_caption(f"{CAPTION}")
        pygame.display.flip()

        self.iteration += 1
        self.clock.tick(FPS)
        self.algorithm_state.update()

    def txt_info(self):
        title = self.font.render(f'{self.algorithm_state.title}', True, BLACK)
        iterations = self.font.render(f'iterations: {self.iteration}', True, BLACK)
        array_len = self.font.render(f'array len: {ARRAY_LEN}', True, BLACK)
        self.screen.blit(title, (20, 10))
        self.screen.blit(iterations, (20, 55))
        self.screen.blit(array_len, (20, 75))

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

    def run(self):

        while self.running:
            self.draw()
            self.txt_info()
            self.update()
            self.check_event()



