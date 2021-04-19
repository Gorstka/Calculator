import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record: Record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        get_today = sum(record.amount for record in self.records
                        if record.date == today)
        return get_today

    def get_week_stats(self):
        today = dt.date.today()
        week = today - dt.timedelta(days=7)
        get_week = sum(record.amount for record in self.records
                       if today >= record.date > week)
        return get_week


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        today_stats = self.get_today_stats()
        calories_remained = self.limit - today_stats
        if today_stats < self.limit:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    'но с общей калорийностью не более '
                    f'{calories_remained} кКал')
        return 'Хватит есть!'


class CashCalculator(Calculator):
    RUB_RATE = 1.00
    USD_RATE = 80.00
    EURO_RATE = 90.00

    def get_today_cash_remained(self, name):
        currency = {'rub': (self.RUB_RATE, 'руб'),
                    'usd': (self.USD_RATE, 'USD'),
                    'eur': (self.EURO_RATE, 'Euro'),
                    }
        if name not in currency:
            raise ValueError('Калькулятор не проводит операции с этой валютой')
        today_stats = self.get_today_stats()
        cash = abs(self.limit - today_stats)
        cash_remained = (round(cash / currency[name][0], 2))
        if today_stats < self.limit:
            return (f'На сегодня осталось {cash_remained} '
                    f'{currency[name][1]}')
        elif today_stats > self.limit:
            return ('Денег нет, держись: твой долг - '
                    f'{cash_remained} {currency[name][1]}')
        return 'Денег нет, держись'


if __name__ == '__main__':
    r1 = Record(amount=145.554, comment='кофе')
    r2 = Record(amount=300.894, comment='Серёге за обед')
    r3 = Record(amount=3000, comment='бар в Танин др', date='08.11.2019')
    cash_calculator = CashCalculator(700)
    cash_calculator.add_record(r1)
    cash_calculator.add_record(r2)
    cash_calculator.add_record(r3)
    print(cash_calculator.get_today_cash_remained('gpb'))
