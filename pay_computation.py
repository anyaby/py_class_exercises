
def main():
    hrs = input('Enter number of hours')

    try:
        hrs = float(hrs)
    except:
        print ('Error, please enter numeric input')
        return

    rate = input('Enter hourly rate')
    try:
        rate = float(rate)
    except:
        print ('Error, please enter numeric input')
        return

    pay = (hrs*rate)
    if hrs>40:
        pay = (1.5*40*rate+(hrs-40)*rate)
        print('Counting overtime hours, your pay is', pay)
    if hrs<=40:
        pay = (hrs*rate)
        print ('Your pay is', pay)
main()
