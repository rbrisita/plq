import sys
import requests
import urllib.parse
'''
Command line client to test against Pig Latin Query API service.
'''

# Check command line arguments
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <ip:port> <pig_latin_query>")
    sys.exit(1)

host = sys.argv[1]
plq = sys.argv[2]

# Prepare URL request
url = f"http://{host}/api/plq/{urllib.parse.quote_plus(plq)}"
print(url)

response = requests.get(url)
if response:
    dic = response.json()
    dic = dic['data']
    print(f"{dic['plq']} = {dic['result']}")
else:
    print('An error has occurred. Please try again.')
