import datetime;
print(dir(datetime))


from datetime import datetime;
now = datetime.now();
print(now)

year = now.year;
print(year)




month = now.month;
print(month)


hour = now.hour;
print(hour)

day=now.day;


minute = now.minute;
print(minute)


second = now.second;
print(second)

# strftime

print(f"{year}/{month}/{day}")