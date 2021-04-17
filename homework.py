import datetime as dt
import math
class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.today().strptime(date, '%d.%m.%Y').date()
    #pass
class Calculator:
    #
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    #
    def add_record(self, record: Record):
        self.records.append(record)
    #
    def get_today_stats(self):
        get_today = 0
        today = dt.datetime.today().date()
        for record in self.records:
            if record.date == today:
                get_today += record.amount 
        return get_today
    #              
    def get_week_stats(self):
        get_week = 0
        today = dt.datetime.today().date()
        week = (dt.datetime.today().date() - dt.timedelta(days=7))
        for record in self.records:
            if today >= record.date >= week:
                get_week += record.amount
        return get_week
    #pass
class CaloriesCalculator(Calculator):
    #
    def __init__(self, limit):
        super().__init__(limit)
    #
    def get_calories_remained(self):
        today_stats = self.get_today_stats()
        calories_remained = self.limit - today_stats
        if today_stats < self.limit:
            return ("Сегодня можно съесть что-нибудь ещё, "
                    "но с общей калорийностью не более "
                    "{} кКал".format(calories_remained))
        else:
            return "Хватит есть!"
    #pass
class CashCalculator(Calculator):
    RUB_RATE = 1.00
    USD_RATE = 60.00 
    EURO_RATE = 70.00
    currency = {'rub': (RUB_RATE, 'руб'),
                'usd': (USD_RATE, 'USD'),
                'eur': (EURO_RATE, 'Euro'),
                }
    def __init__(self, limit):
        super().__init__(limit)
        self.USD_RATE: Union[int, float]
        self.EURO_RATE: Union[int, float]
    def get_today_cash_remained(self, name):
        cash_remained: Union[int, float] = 0.00
        if name in self.currency:
            today_stats = self.get_today_stats()            
            cash = math.fabs(self.limit - today_stats) 
            cash_remained = (round(cash / self.currency[name][0], 2))  
            if today_stats < self.limit:
                return (f'На сегодня осталось {cash_remained} '
                        f'{self.currency[name][1]}')
            elif today_stats > self.limit:
                return (f'Денег нет, держись: твой долг - '
                        f'{cash_remained} {self.currency[name][1]}')
            else:
                return f'Денег нет, держись'

#calories_calculator = CaloriesCalculator(300)
r1 = Record(amount=145.554, comment='кофе')
r2 = Record(amount=300.894, comment='Серёге за обед')
r3 = Record(amount=3000, comment='бар в Танин др', date='08.11.2019')
#calories_calculator.add_record(r1)
#calories_calculator.add_record(r2)
#calories_calculator.add_record(r3)
#print(calories_calculator.get_calories_remained())
cash_calculator = CashCalculator(700)
cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
cash_calculator.add_record(r3)
print(cash_calculator.get_today_cash_remained('eur'))