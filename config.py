# -*- coding: utf-8 -*-

import json

class Config():
    """The main configurations of the simulation"""
    def __init__(self):

        with open('settings.json') as f:
            data = json.load(f)
        # Исходные данные:
        # 	Заразность (infection rate) 90%
        self.inf_rate = data['inf_rate']
        # 	Смертность (mortality rate) 7%
        self.mort_rate = data['mort_rate']
        # 	Вероятность повторного заражения (re-infection rate) 70%
        self.reinf_rate = data['reinf_rate']
        # 	Эффективность вакцины (vaccine efficacy) 60% (вакцинированный человек с указанной вероятностью НЕ заразится при контакте с зараженным)
        self.vac_eff = data['vac_eff']
        # День старта вакцинации
        self.vaccination = data['vaccination']
        # 	Инкубационный период (incubation period) 2 недели (14 секунд в симуляции)
        self.inc_period = data['inc_period']
        # Исходная численность населения
        self.initial_population = data['init_pop']
        # Население на самоизоляции
        self.isolated = data['isolated']


        # Цвета
        # Здоровые (healthy)
        self.healthy_color = (39, 174, 96)
        # Заразившиеся (infected)
        self.infected_color = (231, 76, 60)
        # Вакцинированные (vaccinated)
        self.vaccinated_color = (155, 89, 182)
        # Переболевшие (recovered)
        self.recovered_color = (243, 156, 18)
        # Исходное население
        self.init_pop_color = (149, 165, 166)
        # Текущее население
        self.current_pop_color = (189, 195, 199)
        # Погибшие
        self.dead_color = (127, 140, 141)
        # Прошедшие дни (до полного выздоровления)
        self.days_color = (52, 152, 219)

        # Данные Pygame
        # Основной экран
        self.caption = "Вакцинирироваться нельзя пускать на самотёк"
        self.FPS = 30
        self.screen_size = {'width': 1920, 'height': 1080}

        # Высота панели статистики
        # self.stat_height = 40

        # Настройки испытательного полигона
        # self.polygon_size = {'width': self.screen_size['width'], 'height': self.screen_size['height'] - self.stat_height}
        self.polygon_size = {'width': self.screen_size['width'], 'height': self.screen_size['height']}
        # self.polygon_bg = (236, 240, 241)
        self.polygon_bg = (6, 0, 1)

        # Настройки панели статистики
        # self.stat_size = {'width': self.screen_size['width'], 'height': self.stat_height}
        # self.stat_bg = (52, 73, 94)
        # self.font_family = 'fonts/ShareTechMono-Regular.ttf'
        # self.font_family = 'fonts/RobotoMono-Regular.ttf'
        self.font_family = 'fonts/KellySlab-Regular.ttf'
        self.font_size = 16
        self.font_color = (189, 195, 199)
