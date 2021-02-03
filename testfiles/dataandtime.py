import datetime
def _get_time(today_hours):
    return datetime.datetime.strptime(today_hours, '%H:%M').time()

gt = _get_time("10:30")    
print(gt)
print(datetime.date.today())
print(datetime.time())