# Напишите функцию, которая определяет сколько сейчас лет пользователю

from datetime import date
year, month, day = 2000, 1, 1
today = date.today()
birth_date = date(year, month, day)
age = today.year - birth_date.year
print(age)
