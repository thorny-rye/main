from threading import Thread
import requests
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f"{self.name}, на нас напали!")
        enemy = 100
        day = 0
        while enemy != 0:
            enemy -= self.power
            day += 1
            sleep(1)
            print(f"{self.name} сражается {day}день(дня)..., осталось {enemy} воинов.")
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()