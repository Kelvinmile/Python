def computepay(hours, rate):
    try:
        fh = float(hours)
    except:
        fh = -1

    try:
        fr = float(rate)
    except:
        fr = -1

    if fh > 40:
        regp = fr*40
        otp = (fh-40)*(fr*1.5)
        pay = regp+otp
    else:
        pay = fh*fr
    return pay

sh = input('Enter Hours: ')
sr = input('Enter Rate: ')

print('Pay: ', computepay(sh, sr))