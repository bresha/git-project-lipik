'''
9. Napišite algoritam koji prima nasumičan pozitivni broj manji od 86400 te pretvara taj broj iz sekunda i ispisuje koliko je to točno vrijeme u satima, minutama i sekundama
'''

import random

seconds = random.randint(0, 86400 - 1)


hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
      
print("%d:%02d:%02d" % (hour, minutes, seconds))

