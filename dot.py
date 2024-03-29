# -*- coding: utf-8 -*-

import pygame, random


from config import Config

class Dot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.color = ''

        self.dot_size = 12

        self.rect = pygame.Rect(random.randint(self.dot_size, self.config.polygon_size['width'] - self.dot_size-5), random.randint(self.dot_size, self.config.polygon_size['height'] - self.dot_size), self.dot_size, self.dot_size)
        # Продолжительность болезни
        self.day = 0
        self.speed = 5

        # Скорость передвижения разных точек
        self.x_velocity, self.y_velocity = random.randint(-self.speed,self.speed), random.randint(-self.speed,self.speed)

    def update(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
        if self.rect.top <= 0 or self.rect.bottom >= self.config.polygon_size['height']:
            self.y_velocity *= -1
        if self.rect.right >= self.config.polygon_size['width'] or self.rect.left <= 0:
            self.x_velocity *= -1
        # print(self.x_velocity, self.y_velocity)
