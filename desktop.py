from plyer import notification
import requests
from datetime import datetime

now = datetime.now()
hour = now.hour
minutes = now.minute
 
 
target_hour = 5
target_minute = 30


def cryptoprice():
    URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(URL)
    data = response.json()
    if response.status_code == 200:
         notification.notify(
            title="Crypto Price Alert 🚨",
            message = f"Bitcoin Price : ${data['bitcoin']['usd']}",
            timeout = 10,
            toast = False
        )
        
        



if __name__ == "__main__":
    cryptoprice()
      
