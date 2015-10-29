from datetime import date, time, datetime, timedelta

d = date(year=2015, month=10, day=29)
t = time(hour=16, minute=30)
print d
print t
dt = datetime.combine(d, t)
print dt
print dt.strftime("%A, %d. %B %Y %H:%M")

dt2 = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print dt2

print datetime.now()
print datetime.utcnow()
print "====special 4 Viktor!===="
td = timedelta(days=1, hours=6)

dt = dt - 3 * td
print dt.strftime("%A, %d. %B %Y %H:%M")