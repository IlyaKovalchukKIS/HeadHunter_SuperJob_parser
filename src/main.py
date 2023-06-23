from pprint import pprint

from src.classes.api_superjob import ApiSuperJob
from src.classes.api_headhunter import ApiHeadHunter
import os

api_key_sj = os.getenv("X_API_APP_ID_KEY")


response_sj = ApiSuperJob('Краснодар', 'Python').api_connect(api_key_sj)

response_hh = ApiHeadHunter('Краснодар', 'Python').api_connect()
