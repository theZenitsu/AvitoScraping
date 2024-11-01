from selenium.webdriver.chrome.options import Options
import random
from fake_useragent import UserAgent

def _create_driver_with_proxy():
        # Liste de proxies
        proxies = [

                  "23.236.170.186:9219"
                   "77.83.233.163:6781"
                    "64.137.31.38:6652"



                ]
        # Sélectionner un proxy et un User-Agent aléatoires
        proxy = random.choice(proxies)
        user_agent = UserAgent().random

        # Configurer les options du navigateur
        options = webdriver.ChromeOptions()
        options.add_argument(f'--proxy-server={proxy}')
        options.add_argument(f'user-agent={user_agent}')

    

