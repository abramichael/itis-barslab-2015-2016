#! coding: utf-8
from datetime import timedelta, datetime, time, date
import requests
import re
r = requests.get("http://fedcsis.org/2014/program")

time_re = r'([01][0-9]|2[0-3])\:([0-5][0-9])'
all_time = timedelta()
base_re =  r"(?P<time1>%s) – (?P<time2>%s)" % (time_re, time_re)
print base_re
pattern = re.compile(base_re)
for item in re.finditer(pattern, r.text.encode(r.encoding)):

    print item.group("time1")
    print item.group("time2")

    hours, minutes = map(int, [item.group(2), item.group(3)])
    dt1 = datetime.combine(date.today(), time(hour=hours, minute=minutes))

    hours, minutes = map(int, [item.group(5), item.group(6)])
    dt2 = datetime.combine(date.today(), time(hour=hours, minute=minutes))

    all_time += (dt2 - dt1)

print all_time
