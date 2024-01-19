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
STRING_SESSION1 = getenv("STRING_SESSION1", "BQDEZbSEDYSggI8J4V7Nt4F7k8GjuyLWriu_qRLmgK0VzK4ctR7jryPQw5AWVOPhOGGghDc-lCazH_qSHIBxCgwQBGVhAcVhVk5yb76CdLNPONGq14wAMOeebpPniY6o2JXmHR6ANGY5R8HQq6Nk3I_XrlzQsYDbtWSkJlWA8pMoGrfabRdOUOff1Wx2v7mLbcXdkW3ACfv87IN3Rs94IWTLX1M4-5wB6GunaUn-rNgLSWjsbCOwb-NIpi5Ly__BrrYYx-s8kCC6b1f14Y8o5wSPKs7wZmB9ruSMvjCj_rIYbGbES2C6isr7xWNE8ClM7TvVrX9JyTxBTTUGcFoDtkpEAAAAAZHvMEMA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
