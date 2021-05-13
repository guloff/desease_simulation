# -*- coding: utf-8 -*-

import pygame
import pygame, sys
import json
import matplotlib.pyplot as plt
import random
import datetime
import time


from config import Config
from dot import Dot

class Vaccination():
    '''Симуляция развития различных сценариев распространения заболевания
    с учетом самоизоляции и вакцинации, а также без их использования'''
    def __init__(self):
        pygame.init()
        self.config = Config()
        # % людей на карантине
        # self.carantin = int(input('Доля населения на самоизоляции (0%): ') or '0') / 100

        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.config.caption)
        # self.screen = pygame.display.set_mode((self.config.screen_size['width'], self.config.screen_size['height']))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.mouse.set_visible(False)

        # Поверхности
        # Поверхность полигона
        self.polygon = pygame.Surface([self.config.polygon_size['width'], self.config.polygon_size['height']])
        # Поверхность панели статистики
        # self.stat = pygame.Surface([self.config.stat_size['width'], self.config.stat_size['height']])
        self.stat_font = pygame.font.Font(self.config.font_family, self.config.font_size)

        # Группы
        # Здоровые (healthy)
        self.healthy = pygame.sprite.Group()
        for i in range(self.config.initial_population - 1):
            new_dot = Dot()
            new_dot.color = self.config.healthy_color
            self.healthy.add(new_dot)


        if self.config.isolated > 0.0:
            # Симуляция самоизоляции (определенная часть населения никуда не ходит)
            count = 0
            for dot in self.healthy:
                count += 1
                if count <= int(len(self.healthy) * self.config.isolated):
                    dot.x_velocity = 0
                    dot.y_velocity = 0

        self.station_horizontal = pygame.sprite.Sprite()
        self.station_vertical = pygame.sprite.Sprite()
        # Заразившиеся (infected)
        self.infected = pygame.sprite.Group()
        new_dot = Dot()
        new_dot.color = self.config.infected_color
        self.infected.add(new_dot)
        # Погибшие
        self.dead = pygame.sprite.Group()
        # Вакцинированные (vaccinated)
        self.vaccinated = pygame.sprite.Group()
        # Переболевшие (recovered)
        self.recovered = pygame.sprite.Group()


        self.counter = 0
        self.days_spent = 0
        self.data = [{'total': 0, 'healthy': 0, 'infected': 0, 'dead': 0, 'vaccinated': 0, 'recovered': 0, 'isolated': 0, 'days': 0}]

        self.item = dict()

    def run(self):
        while True:
            self._check_events()
            self.days_counter()

            # Заполнение поверхностей полигона и статистики
            self.polygon.fill(self.config.polygon_bg)
            # self.stat.fill(self.config.stat_bg)

            self._draw_healthy()
            self._draw_recovered()
            self._draw_infected()
            self._draw_vaccinated()
            self._show_stat()


            if self.config.vaccination < self.days_spent < 10000:
                # Станция вакцинации
                self.station_vertical.rect = pygame.Rect((0,0,self.config.screen_size['width'],10))
                pygame.draw.rect(self.polygon, self.config.vaccinated_color, self.station_vertical.rect)

                self.station_horizontal.rect = pygame.Rect((self.config.screen_size['width']-10, 0,10,self.config.screen_size['height']))
                pygame.draw.rect(self.polygon, self.config.vaccinated_color, self.station_horizontal.rect)

                collided_healthy_v = pygame.sprite.spritecollide(self.station_vertical, self.healthy, False)
                if collided_healthy_v:
                    for dot in collided_healthy_v:
                        self.healthy.remove(dot)
                        self.vaccinated.add(dot)
                        dot.color = self.config.vaccinated_color

                collided_healthy_h = pygame.sprite.spritecollide(self.station_horizontal, self.healthy, False)
                if collided_healthy_h:
                    for dot in collided_healthy_h:
                        self.healthy.remove(dot)
                        self.vaccinated.add(dot)
                        dot.color = self.config.vaccinated_color

            # Отображение поверхностей полигона и статистики
            self.screen.blit(self.polygon, (0,0))
            # self.screen.blit(self.stat, (0, self.config.polygon_size['height']))

            pygame.display.flip()
            self.record_data(len(self.healthy), len(self.infected), len(self.dead), len(self.vaccinated), len(self.recovered), self.config.isolated, self.days_spent)
            self.clock.tick(self.config.FPS)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.stop()

    def stop(self):
        pygame.quit()
        self.show_plot()
        sys.exit()

    def record_data(self, healthy, infected, dead, vaccinated, recovered, isolated, days):
        self.item = {
            'total': (healthy + infected + recovered +vaccinated),
            'healthy': healthy,
            'infected': infected,
            'dead': dead,
            'vaccinated': vaccinated,
            'recovered': recovered,
            'isolated': isolated,
            'days': days
        }

        if self.item['days'] != self.data[-1]['days']:
            self.data.append(self.item)

    def show_plot(self):
        with open('stat.json', 'w') as f:
            json.dump(self.data, f, indent=4)
        plt.style.use('classic')
        # fig, ax = plt.subplots()
        total = []
        healthy = []
        infected = []
        dead = []
        vaccinated = []
        recovered = []
        days = []

        for item in self.data:
            total.append(item['total'])
            healthy.append(item['healthy'])
            infected.append(item['infected'])
            dead.append(item['dead'])
            vaccinated.append(item['vaccinated'])
            recovered.append(item['recovered'])
            days.append(item['days'])


        plt.plot(days, total, label = 'Total')
        plt.plot(days, healthy, label = 'Healthy')
        plt.plot(days, infected, label = 'Infected')
        plt.plot(days, dead, label = 'Dead')
        plt.plot(days, vaccinated, label = 'Vaccinated')
        plt.plot(days, recovered, label = 'Recovered')

        plt.legend(loc='upper left', frameon=False)
        today = datetime.datetime.now()
        plt.savefig(f'figures/fig_{today.year}-{today.month}-{today.day}_{today.hour}-{today.minute}-{today.second}.png')
        plt.show()

    def days_counter(self):
        self.counter += 1
        if len(self.infected) and self.counter % self.config.FPS == 0:
            self.days_spent += 1

    def _draw_healthy(self):
        self.healthy.update()
        for dot in self.healthy:
            pygame.draw.rect(self.polygon, dot.color, dot.rect)

    def _draw_vaccinated(self):
        self.vaccinated.update()
        for dot in self.vaccinated:
            pygame.draw.rect(self.polygon, dot.color, dot.rect)

    def _draw_recovered(self):
        self.recovered.update()
        for dot in self.recovered:
            pygame.draw.rect(self.polygon, dot.color, dot.rect)

    def _draw_infected(self):
        self.infected.update()
        for dot in self.infected:
            if self.counter % 30 == 0:
                dot.day += 1
            # Проверяем, прошло ли 14 дней со дня заражения
            if dot.day == self.config.inc_period:
                # Если да, то генерируем случайное число
                number = random.randrange(100)
                if number > self.config.mort_rate:
                    # Если оно больше порога смертности, то точка выживает
                    self.infected.remove(dot)
                    # и пененосится в группу выздоровевших
                    self.recovered.add(dot)
                    dot.color = self.config.recovered_color
                else:
                    self.infected.remove(dot)
                    self.dead.add(dot)

            # Проверяем столкновение со здоровыми
            collided_healthy = pygame.sprite.spritecollide(dot, self.healthy, False)
            if collided_healthy:
                for dot in collided_healthy:
                    # Генерируем случайное число
                    number = random.randrange(100)
                    if number <= self.config.inf_rate:
                        self.healthy.remove(dot)
                        self.infected.add(dot)
                        dot.color = self.config.infected_color

            # Проверяем столкновение с переболевшими
            collided_recovered = pygame.sprite.spritecollide(dot, self.recovered, False)
            if collided_recovered:
                for dot in collided_recovered:
                    # Генерируем случайное число
                    number = random.randrange(100)
                    if number <= self.config.reinf_rate:
                        self.recovered.remove(dot)
                        self.infected.add(dot)
                        dot.color = self.config.infected_color
                        dot.day = 0

            # Проверяем столкновение с вакцинированными
            collided_vaccinated = pygame.sprite.spritecollide(dot, self.vaccinated, False)
            if collided_vaccinated:
                for dot in collided_vaccinated:
                    # Генерируем случайное число
                    number = random.randrange(100)
                    if number > self.config.vac_eff:
                        self.vaccinated.remove(dot)
                        self.infected.add(dot)
                        dot.color = self.config.infected_color
                        dot.day = 0

            pygame.draw.rect(self.polygon, dot.color, dot.rect)

    def _show_stat(self):
        total = self.config.initial_population - len(self.dead)

        # self.stat_text = f'Total: {total} | Healty: {len(self.healthy)} | Infected: {len(self.infected)} | Dead: {len(self.dead)} | Vaccinated: {len(self.vaccinated)} | Recovered: {len(self.recovered)} | Days Spent: {self.days_spent}'
        #
        # self.stat_image = self.stat_font.render(self.stat_text, True, self.config.font_color)
        # self.stat.blit(self.stat_image, (10,10))

        # Легенда
        self._show_legend(surface = self.polygon, color = self.config.init_pop_color, text = f'Initial pop.: {self.config.initial_population}', line_x = 180, line_y = 926, line_w = self.config.initial_population, line_h = 6, tx = 6, ty = 920)

        self._show_legend(surface = self.polygon, color = self.config.current_pop_color, text = f'Current pop.: {total}', line_x = 180, line_y = 946, line_w = total, line_h = 6, tx = 6, ty = 940)

        self._show_legend(surface = self.polygon, color = self.config.healthy_color, text = f'Healthy: {len(self.healthy)}', line_x = 180, line_y = 966, line_w = len(self.healthy), line_h = 6, tx = 6, ty = 960)

        self._show_legend(surface = self.polygon, color = self.config.infected_color, text = f'Infected: {len(self.infected)}', line_x = 180, line_y = 986, line_w = len(self.infected), line_h = 6, tx = 6, ty = 980)

        self._show_legend(surface = self.polygon, color = self.config.vaccinated_color, text = f'Vaccinated: {len(self.vaccinated)}', line_x = 180, line_y = 1006, line_w = len(self.vaccinated), line_h = 6, tx = 6, ty = 1000)

        self._show_legend(surface = self.polygon, color = self.config.recovered_color, text = f'Recovered: {len(self.recovered)}', line_x = 180, line_y = 1026, line_w = len(self.recovered), line_h = 6, tx = 6, ty = 1020)

        self._show_legend(surface = self.polygon, color = self.config.dead_color, text = f'Dead: {len(self.dead)}', line_x = 180, line_y = 1046, line_w = len(self.dead), line_h = 6, tx = 6, ty = 1040)

        self._show_legend(surface = self.polygon, color = self.config.days_color, text = f'Days Spent: {self.days_spent}', line_x = 180, line_y = 1066, line_w = self.days_spent, line_h = 6, tx = 6, ty = 1060)

    def _show_legend(self, surface, color, text, line_x, line_y, line_w, line_h, tx, ty):
        pygame.draw.rect(surface, color, (line_x,line_y,line_w,line_h))
        image = self.stat_font.render(text, True, color)
        surface.blit(image, (tx, ty))

if __name__ == '__main__':
    inf_rate = int(input('Вероятность заражения при контакте (20%): ') or '20')
    mort_rate = int(input('Смертность (15%): ') or '15')
    reinf_rate = int(input('Вероятность повторного заражения (10%): ') or '10')
    vaccination = int(input('День старта вакцинации (10001) / (>10_000 - никогда): ') or '10001')
    vac_eff = int(input('Эффективность вакцины (95%): ') or '95')
    inc_period = int(input('Инкубационный период (14 дней): ') or '14')
    init_pop = int(input('Население (1000 человек): ') or '1000')
    isolated = int(input('Доля населения на самоизоляции (0%): ') or '0') / 100


    data = {
        'inf_rate': inf_rate,
        'mort_rate': mort_rate,
        'reinf_rate': reinf_rate,
        'vaccination': vaccination,
        'vac_eff': vac_eff,
        'inc_period': inc_period,
        'init_pop': init_pop,
        'isolated': isolated,
    }

    with open('settings.json', 'w') as f:
        json.dump(data, f, indent = 4)

    vac = Vaccination()
    vac.run()
