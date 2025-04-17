power = 2
act = 1
counter = 1
for i in range(256):
    summmy = power + act
    print(f'{counter}: {power} + {act} = {summmy}')
    act = power
    power += power
    counter += 1
     
