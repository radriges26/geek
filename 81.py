# Реализовать класс «Дата»

class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    def __str__(self):
        return f"Дата: {self.str_date}"

    @classmethod
    def get_date(cls, str_date):
        day = int(str_date.split("-")[0])
        month = int(str_date.split("-")[1])
        year = int(str_date.split("-")[2])
        return day, month, year

    @staticmethod
    def check_date(str_date):
        print(f"Дата для проверки: {str_date}")
        day = int(str_date.split("-")[0])
        month = int(str_date.split("-")[1])

        if 0 < day <= 31:
            print("День указан верно")
        else:
            print("День указан неверно")

        if 0 < month <= 12:
            print("Месяц указан верно")
        else:
            print("Месяц указан неверно")

        print("Год проверять не надо")


d = Date("31-03-2020")

print(d, end="\n\n")

print(d.get_date("23-11-1974"), end="\n\n")  # преобразование даты к числовому формату

Date.check_date("11-12-2005")  # валидация даты
