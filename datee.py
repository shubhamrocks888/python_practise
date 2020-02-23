import datetime
import pytz
# d = datetime.date(2015,5,1)
# d = datetime.date.today()
# d.day,d.year,d.month
# print (d.weekday())     Monday 0 Sunday 6
# print (d.isoweekday())  Monday 1 Sunday 7
# tdelta = datetime.timedelta(days=4)
# print (d + tdelta)
# print (d - tdelta)
# tdelta = datetime.timedelta(days=4) {use days,hours,minutes,seconds,microseconds}
# print (d + tdelta)
# bday = datetime.date(1992,7,15)
# till = d -bday
# print (till)    10072 days, 0:00:00
# print (till.days)  10072
# print print (till.total_seconds())  870220800.0
# print (till.total_seconds())
# t = datetime.time(9,15,30,1234)       09:15:30.001234
# t.hour,t.minute,t.second,t.microsecond....
# t = datetime.datetime(2015,8,28,9,15,30,1234)     2015-08-28 09:15:30.001234
# t.date()      2015-08-28
# t.time()      09:15:30.001234
# t.minute,t.day,t.year,t.hour,t.second,t.microsecond
# t = datetime.datetime(2015,8,28,9,15,30,1234) tdelta = datetime.timedelta(days=7)   2015-09-04 09:15:30.001234
# tdelta = datetime.timedelta(hours=7)
# dt_today = datetime.datetime.today()  datetime without timezone   2020-02-11 23:21:18.808784
# dt_now = datetime.datetime.now() datetime with timezone(rightnow it is empty) 2020-02-11 23:21:18.808839
# dt_utcnow = datetime.datetime.utcnow() datetime with timezone(rightnow it is empty)   2020-02-11 17:51:18.808842
# import pytz for timezone
# dt = datetime.datetime(2016,8,7,1,45,35,1886,tzinfo=pytz.UTC) 2016-08-07 01:45:35.001886+00:00
# dt_now = datetime.datetime.now(tz=pytz.UTC)   2020-02-11 18:09:11.298141+00:00
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)   2020-02-11 18:11:14.153859+00:00
# dt_mtn = datetime.datetime.now(pytz.timezone('US/Mountain'))    2020-02-11 11:14:57.202005-07:00
# for tz in pytz.all_timezones:
#     print (tz) -->   Asia/Calcutta   US/Mountain
#naive time = time without timezone
# dt_mtn = datetime.datetime.now()    2020-02-12 00:02:26.760642
# dt_east = dt_mtn.astimezone( pytz.timezone('Asia/Calcutta'))  2020-02-12 00:03:28.392430+05:30
# strftime --> convert datetime into Strimg
# strptime --> convert datetime string into datetime object

# dt_str = '2020-02-11 23:48:54.358220+05:30'
# dt = datetime.datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S.%f%z') 2020-02-11 23:48:54.358220+05:30
# dt_mtn = datetime.datetime.now(tz=pytz.timezone('Asia/Calcutta')) 2020-02-12 00:29:06.477788+05:30
# dt = dt_mtn.strftime('%B %d, %Y') February 12, 2020
# dt_mtn = datetime.datetime.now(tz=pytz.timezone('Asia/Calcutta'))
# dt = dt_mtn.strftime('%B %d, %Y')
# print ("hello")