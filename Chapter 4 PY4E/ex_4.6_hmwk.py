def computepay(h, r):
    if h < 40:
        pay = (h*r)
    else:
        overtime = h - 40
        ot = float(overtime)
        pay = (40*r) + (ot*r*1.5)
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)