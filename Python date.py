#Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta

today = datetime.now()
five_days_ago = today - timedelta(days=5)

print("Текущая дата:", today)
print("Дата, вычтя 5 дней:", five_days_ago)

#Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Вчера:", yesterday)
print("Сегодня:", today)
print("Завтра:", tomorrow)

#Write a Python program to drop microseconds from datetime.
from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print("Текущее время с микросекундами:", now)
print("Текущее время без микросекунд:", no_microseconds)

#Write a Python program to calculate two date difference in seconds.
from datetime import datetime

# Пример двух дат (можно изменить на нужные значения)
date1 = datetime(2025, 1, 1, 12, 0, 0)
date2 = datetime(2025, 1, 1, 14, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Разница в секундах:", seconds)
