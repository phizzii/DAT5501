import sys
print(sys.path)

import random
from datetime import datetime, timedelta
from sophie import sophi
import time

doggie = Pet('doggie','cute little terrier, very naughty')

#doggie.get_hunger()
#doggie.feed_pet()

hunger = 100
hunger_rate = 1

while hunger >= 0: #problem: it won't do anything due to time sleep & until time sleep is finished, code is stuck waiting
    hunger = hunger - random.randint(0,10)#
    time.sleep(30)
    print(hunger)
    if hunger <= 20:
        print("[!!!] your little friend is getting really hungry over here [!!!]")