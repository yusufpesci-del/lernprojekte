import sys
import requests
from secret import API_KEY


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}")
except requests.RequestException:
    sys.exit("Request failed")

data = response.json()
price = float(data["data"]["priceUsd"])

print(f"${bitcoins * price:,.4f}")
