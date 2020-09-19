import time
import random

print('Enter Username:')
username = str(input())
print('\nWelcome to Clout Trading\n', username, 'pick a lucky number you fool ???')
t = int(input())

def createList(r1, r2):
    return list(range(r1, r2 + 1))
r1, r2, r3, r4 = 0, 200, 500, 1000
prices = createList(r1, r2)
prices2 = createList(r2, r3)
prices3 = createList(r3, r4)

progress = 0
responce1 = 'System said : "Fuck what you say, We doing it pussy!!!!"'
responce2 = 'System said : "YOU SUCK AT TRADING"'

while t:
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print('Clout loading.....', progress, '%    time left =', timeformat, end='\r')
    time.sleep(.5)
    t -= 1
    progress += 4
else:
    print('want to buy some stocks ????')
    decision = str(input())
    print('how many to buy??')
    stocks = int(input())
    print(username, 'said', decision, '\n', responce1, '\nBuying ', stocks, 'stocks')
    for countdown in reversed(range(stocks + 1)):
        if countdown > 0:
            print(countdown, end='...Shares left to buy\r')
            time.sleep(1)
        else:
            print('Shares brought at = ')
            print('APPL: $', random.choice(prices), '\nTSLA: $', random.choice(prices2), '\nAMZN: $', random.choice(prices3))


print('\n DO YOU WANT TO SELL THE STOCKS ???')
sellDecision = str(input())
print('HOW MANY YOU GONNA SELL')
sellstocks= int(input())
print(username, 'said', sellDecision, '\n System says - >', responce2)
for countdown in reversed(range(sellstocks + 1)):
    if countdown > 0:
        print(countdown, end='......Shares left to sell\r')
        time.sleep(1)
    else:
        print('\nShares sold at = ')
        print('APPL: $', random.choice(prices), '\nTSLA: $', random.choice(prices2), '\nAMZN: $', random.choice(prices3))

