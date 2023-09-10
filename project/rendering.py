from random import randint

import pygame

from .models import Pipe, Score, bird, TopPipe, BottomPipe
from . import settings
from . import textures


# pygame.init()


class Renderer:
    def __init__(self):
        self.background_blocks = [pygame.Rect(0, 0, 288, 600), ]
        self.frame = 0
        self.score = 0
        self.pipes = []
        self.pipes_score = []
        self.state = 'start'

    def draw_score(self):
        score_text = Score(self.score)
        textures.screen.blit(score_text.text, (settings.WINDOW_WIDTH // 2, 30))

    def draw_background(self):
        for bg in self.background_blocks:
            textures.screen.blit(textures.background_block, bg)

    def draw_bird(self):
        self.frame = (self.frame + 0.2) % 4
        img_bird = textures.bird_frames.subsurface(34 * int(self.frame), 0, 34, 24)
        if self.state == 'play':
            img_bird = pygame.transform.rotate(img_bird, -bird.fall_speed * 3)
        textures.screen.blit(img_bird, bird.model)

    def draw_pipes(self):
        for pipe in self.pipes:
            if pipe.model.y == 0:
                rect = textures.pipe_top.get_rect(bottomleft=pipe.model.bottomleft)
                textures.screen.blit(textures.pipe_top, rect)
            else:
                rect = textures.pipe_bottom.get_rect(topleft=pipe.model.topleft)
                textures.screen.blit(textures.pipe_bottom, rect)

    def update_score(self):
        for pipe in self.pipes:
            if pipe.model.right < bird.model.left and pipe not in self.pipes_score:
                self.pipes_score.append(pipe)
                self.score += 0.5

    def collisions(self):
        for pipe in self.pipes:
            if bird.model.colliderect(pipe.model) or bird.model.top < 0 or bird.model.bottom > settings.WINDOW_HEIGHT:
                self.state = 'start'
                self.score = 0

    def pipe_spawn(self):
        if self.state == 'play':
            if len(self.pipes) == 0 or self.pipes[-1].model.x < settings.WINDOW_WIDTH - 200:
                random_height = randint(100, 300)
                self.pipes.append(TopPipe(random_height))
                self.pipes.append(BottomPipe(random_height))

    def pipe_remove(self, pipe):
        self.pipes.remove(pipe)
        if pipe in self.pipes_score:
            self.pipes_score.remove(pipe)

    def pipe_movement(self):
        for pipe in reversed(self.pipes):
            pipe.model.x -= 5

            if pipe.model.right < 0:
                self.pipe_remove(pipe)

    def background_spawn(self):
        if self.background_blocks[-1].right <= settings.WINDOW_WIDTH:
            self.background_blocks.append(pygame.Rect(self.background_blocks[-1].right, 0, 288, 600))

    def background_remove(self, bg):
        if bg.right < 0:
            self.background_blocks.remove(bg)

    def background_movement(self):
        for bg in reversed(self.background_blocks):
            bg.x -= 1
            self.background_remove(bg)

    def game_stage(self):
        if self.state == 'start':
            self.pipes = []
            bird.model.y = settings.WINDOW_HEIGHT // 2
        elif self.state == 'play':
            bird.fall_speed += 1
            bird.model.y += bird.fall_speed
