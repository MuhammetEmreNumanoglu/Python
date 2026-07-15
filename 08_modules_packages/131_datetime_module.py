import datetime

today = datetime.date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

now = datetime.datetime.now()
print("Now:", now)
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

birthday = datetime.date(1990, 6, 15)
age_days = (today - birthday).days
print("Days since 1990-06-15:", age_days)

future = today + datetime.timedelta(days=30)
print("30 days from now:", future)

parsed = datetime.datetime.strptime("2024-01-15", "%Y-%m-%d")
print("Parsed:", parsed)
