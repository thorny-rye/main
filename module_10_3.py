import random
from time import sleep
from threading import Thread, Lock


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        refill = random.randint(50, 500)
        for i in range(100):
            self.balance += refill
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {refill}. Баланс: {self.balance}" + '\n')
            sleep(0.001)

    def take(self):
        take_money = random.randint(50, 500)
        for i in range(100):
            print(f"Запрос на {take_money}" + "\n")
            self.balance -= take_money
            if take_money <= self.balance:
                self.balance -= take_money
                print(f"Снятие: {take_money}. Баланс: {self.balance}" + "\n")
            else:
                print("Запрос отклонён, недостаточно средств" + "\n")
                self.lock.acquire()
                sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
