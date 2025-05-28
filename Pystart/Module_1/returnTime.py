# This is script to convert seconds to Time HH:MM format
import math

seconds = int(input('Input time in seconds: '))
seconds_truncated = seconds % (60 * 60 * 24)

HH = seconds_truncated // 3600
MM = math.floor((seconds_truncated - HH * 3600) / 60)

if(HH < 10):
    hours = '0' + str(HH)
else:
    hours = str(HH)
if(MM < 10):
    minutes = '0' + str(MM)
else:
    minutes = str(MM)

print(f'{hours}:{minutes}')



