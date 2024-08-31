num = int(input('Введіть число більше або дорівнює 0 і менше ніж 8640000: '))

days_seconds = 86400
hours_seconds = 3600
minutes_seconds = 60

days, remainder = divmod(num, days_seconds)
hours, remainder = divmod(remainder, hours_seconds)
minutes, seconds = divmod(remainder, minutes_seconds)

if days == 1:
    what_day = 'день'
elif 2 <= days <= 4:
    what_day = 'дні'
else:
    what_day = 'днів'

hours = f'{hours:02}'
minutes = f'{minutes:02}'
seconds = f'{seconds:02}'


print(f'{days} {what_day}, {hours}:{minutes}:{seconds}')