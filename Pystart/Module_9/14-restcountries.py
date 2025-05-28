# Module 9 - Restcountries API

# TASK DESCRIPTION
# Based on API https://restcountries.com Prepare an application that will ask
# user for the name of the country and then display its capital.
# Remember to handle the situation when:
# ● the user enters the name of a country that is not in the database.
#  ● the script will not have access to the Internet
#  It is also worth considering what should happen when the user
# will ask the same question twice. Should we ask about them second
# once API? Think about the rationale behind your decision.

# Import libraries
from requests import get, exceptions

country = str(input(f"Give me name of country: "))
url_country = f"https://restcountries.com/v3.1/name/{country.lower()}"

try:
    response = get(url_country)
    capital = response.json()[0]["capital"][0]
    print(capital)
except exceptions.ConnectionError:
    print("There is no connection with internet. Check your connection and try again.")
except KeyError:
    print("Such country doesn't exists in restcountries database.")
