#Напишите функцию, которая определяет какому дню недели соответствует эта дата

>>> import datetime
>>> datetime.datetime.today()
datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
>>> datetime.datetime.today().weekday()
4
From the documentation:Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
