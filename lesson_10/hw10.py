import uuid
import datetime
from art import *


class Bank:
    deposit_bag = 0

    def __init__(self, name, deposit, percent):
        self.name = name
        self.deposit = deposit
        self.__percent = percent
        self.id = uuid.uuid4()
        self.date = datetime.datetime.now()
        Bank.deposit_bag += deposit

    def __str__(self):
        return f'{self.name}, {self.__percent}, {self.deposit}'

    def __del__(self):
        Bank.deposit_bag -= self.deposit
        print(
            f'У {self.name} закрито рахунок у звязку з ліквідацією банка, повернуто {self.deposit}, власник претензій не має')

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, digit):
        if 0 < digit < 100:
            self.__percent = digit
        else:
            raise 'неверное значение процента'

    def add_money(self, amount):
        self.deposit += amount
        Bank.deposit_bag += amount

    def subtract_money(self, amount):
        self.deposit -= amount
        Bank.deposit_bag -= amount

    def transfer(self, other, amount):
        other.deposit += amount
        self.deposit -= amount

    @property
    def get_todays_profit(self):
        daily_profit = self.deposit * (self.__percent / 100) / 365
        return daily_profit

    @staticmethod
    def advertise():
        print(text2art("Your money is in good hands", font='small', chr_ignore=True))

    @classmethod
    def total_cash_in_bank(cls):
        return Bank.deposit_bag


alex = Bank('Alex', 10000, 10)
mark = Bank('Mark', 8000, 15)
alex.percent = 0
alex.add_money(2000)
alex.subtract_money(1000)
alex.transfer(mark, 1000)
