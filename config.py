import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "25272906")) #optional
API_HASH = getenv("API_HASH", "a341f3a7733db7bf7202708926baab42") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6158769611").split()))
OWNER_ID = int(getenv("OWNER_ID", "5686300259"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://techbrou:Pandey2120@cluster1.6ujsngj.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6139945042:AAGMb8-bQKsH_-5pmXClt8ZrUhMg3_fFalc")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/a11b92d11d3b9ab8e77ee.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "UTKARSH")
PM_LOGGER = getenv("PM_LOGGER", "727610771")
LOG_GROUP = getenv("LOG_GROUP", "972249333")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/utkarshrobin/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGBokoAh68attW2dtH50vQkH8E5vvBEGOHZyocduTv7aeRTUVKOaZuD_E_y5YJEyZIktIJ6L9n0nGa8L_eQRViQjTwJycmHPNFLEaV37_ddDWlp_FkaMTtAQ81tMrxOQQUDGi01meq3GnSioDa-LvQi8MA0sNoev2HVe-QqoJhpjjwO0p4lFu3QSwk5OrDRb-7FZAj-i8B58DItovGvDeY7TAow087uCl-Q-5g38_FJHpoP3mMKtnqWZWe9EJ9snn9TbYvniu1ukEbYsuDUg1xCR51BIZbOVHRIDfonZ41V0rqze1okyiSz0ZAzj_1qwYD_nIA0pRG0EbvRfnZ15ylQt4VQxQAAAAFS7g5jAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
