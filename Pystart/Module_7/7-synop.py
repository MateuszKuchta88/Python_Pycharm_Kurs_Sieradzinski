# Module 7 - Get synoptic data

# TASK DESCRIPTION
# Based on data provided free of charge by:
#  https://danepubliczne.imgw.pl/apiinfo
#  Prepare a script that will display information about temperature and
# pressure in the city closest to your place of residence

# Import libraries
from requests import get

# Declare function
url = "https://danepubliczne.imgw.pl/api/data/synop/"
wanted_city = "Warszawa"

for reading in get(url).json():
    if reading.get("stacja") == wanted_city:
        print(f'Temperatura w mieście {wanted_city} wyniosiła {reading.get("temperatura")} stopni Celsiusza.')
        print(f'Natomiast ciśnienie w mieście {wanted_city} wyniosło {reading.get("cisnienie")} hPa.')
