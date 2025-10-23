import datetime

# Time:
t1 = datetime.time(15, 0, 0)
t10 = datetime.time(18, 0, 0)
# print(t10 - t1 ) # No se puede

# Date:
t2 = datetime.date(2025, 10, 20)
t20 = datetime.date(2025, 10, 25)
res = t20 - t2
print(res, type(res))

# Datetime:
t3 = datetime.datetime(2025, 10, 20, 15)
t30 = datetime.datetime(2025, 10, 21, 20)
res = t30 - t3
print(res, type(res))

# Fecha de ahora:
t4 = datetime.datetime.now()
print(t4)

new_time = t4  # new_time es datetime
for x in range(5):
    new_time -= datetime.timedelta(hours=1)
    print(new_time, type(new_time))
