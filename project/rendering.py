from random import randint

import pygame

from .models import Score, bird, TopPipe, BottomPipe
from . import settings
from . import textures


class Game:
    def __init__(self):
        self.score = 0
        self.game_condition = 'start'


class Spawner:
    def __init__(self, game: Game):
        self.game = game
        self.background_rectangles = [pygame.Rect(0, 0, 288, 600), ]
        self.pipes = []
        self.pipes_to_left_of_bird = []

    def update_score(self):
        for pipe in self.pipes:
            if pipe.model.right < bird.model.left and pipe not in self.pipes_to_left_of_bird:
                self.pipes_to_left_of_bird.append(pipe)
                self.game.score += 0.5

    def collisions(self):
        for pipe in self.pipes:
            if bird.model.colliderect(pipe.model) or bird.model.top < 0 or bird.model.bottom > settings.WINDOW_HEIGHT:
                self.game.game_condition = 'start'
                self.game.score = 0

    def pipes_spawn(self):
        if self.game.game_condition == 'play':
            if len(self.pipes) == 0 or self.pipes[-1].model.x < settings.WINDOW_WIDTH - settings.DISTANCE_BETWEEN_PIPES:
                random_height = randint(100, 300)
                self.pipes.append(TopPipe(random_height))
                self.pipes.append(BottomPipe(random_height))

    def pipe_remove(self, pipe):
        self.pipes.remove(pipe)
        if pipe in self.pipes_to_left_of_bird:
            self.pipes_to_left_of_bird.remove(pipe)

    def pipes_movement(self):
        for pipe in reversed(self.pipes):
            pipe.model.x -= 5

            if pipe.model.right < 0:
                self.pipe_remove(pipe)

    def background_spawn(self):
        if self.background_rectangles[-1].right <= settings.WINDOW_WIDTH:
            self.background_rectangles.append(
                pygame.Rect(self.background_rectangles[-1].right, 0, 288, settings.WINDOW_HEIGHT)
            )

    def background_remove(self, bg_rect):
        self.background_rectangles.remove(bg_rect)

    def background_movement(self):
        for bg_rect in reversed(self.background_rectangles):
            bg_rect.x -= 1
            if bg_rect.right < 0:
                self.background_remove(bg_rect)

    def game_stage(self):
        if self.game.game_condition == 'start':
            self.pipes = []
            bird.model.y = settings.WINDOW_HEIGHT // 2
        elif self.game.game_condition == 'play':
            bird.fall_speed += 1
            bird.model.y += bird.fall_speed


class Painter:
    def __init__(self, game: Game, spawner: Spawner):
        self.game = game
        self.spawner = spawner
        self.bird_frame_num = 0

    def draw_background(self):
        for bg_rect in self.spawner.background_rectangles:
            textures.screen.blit(textures.background_img_block, bg_rect)

    def draw_bird(self):
        self.bird_frame_num = (self.bird_frame_num + 0.2) % 4

        img_bird = textures.bird_frames.subsurface(
            settings.BIRD_WIDTH * int(self.bird_frame_num), 0, settings.BIRD_WIDTH, settings.BIRD_HEIGHT
        )

        if self.game.game_condition == 'play':
            img_bird = pygame.transform.rotate(img_bird, -bird.fall_speed * 3)

        textures.screen.blit(img_bird, bird.model)

    def draw_pipes(self):
        for pipe in self.spawner.pipes:
            if type(pipe) == TopPipe:
                rect = textures.pipe_top.get_rect(bottomleft=pipe.model.bottomleft)
                textures.screen.blit(textures.pipe_top, rect)
            else:
                rect = textures.pipe_bottom.get_rect(topleft=pipe.model.topleft)
                textures.screen.blit(textures.pipe_bottom, rect)

    def draw_score(self):
        score = Score(self.game.score)
        textures.screen.blit(score.text, (settings.WINDOW_WIDTH // 2, 30))
