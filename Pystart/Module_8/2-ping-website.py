# Module 8 - Ping some website

# TASK DESCRIPTION
# Get the IP address or domain from the user, e.g. pystart.pl, and then
# execute the system command ping <provided address>
#  e.g. ping pystart.pl
#  Display “Address available” or “Address unavailable”
# depending on whether the address responded or did not respond

# Import libraries
import subprocess


# Testing data
website = input(str("Wprowadź url do weryfikacji: "))

# Declare function


# Tests
output = subprocess.run(["ping", "-n", "1", website], shell=True, capture_output=True).stdout.decode('utf8')


# Print output message
if 'could not find' in output:
    print('Adres jest niedostępny')
else:
    print('Adres jest dostępny')
