import datetime

d = datetime.date.today() - datetime.timedelta(5)
print('current date: ', datetime.date.today())
print('five days before current date: ', d)
