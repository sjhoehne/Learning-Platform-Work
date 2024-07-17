hrs = input('Enter Hours:')
h = float(hrs)
rate = input('Enter Rate:')
r = float(rate)
if h <= 40:
    pay = h*r
else:
    overtime = h - 40
    o = float(overtime)
    pay = (40*r) + (o*r*1.5)
print(pay)