import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "13764765")) #optional
API_HASH = getenv("API_HASH", "0255274ce6771d5535c201dd05ce8d79") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6171318773 6276767659 6104126188").split()))
OWNER_ID = int(getenv("OWNER_ID", "6290258924"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://techbrou:pandey2120@cluster0.oog5hnb.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6288784069:AAFNIMutl1UjKNh9Tegp7POUWk2PRV3_Uk8")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/a11b92d11d3b9ab8e77ee.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "UTKARSH")
PM_LOGGER = getenv("PM_LOGGER", "727610771")
LOG_GROUP = getenv("LOG_GROUP", "972249333")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGVS9IAKPVWLvokUjDIf084GIurOabC5hy64dTUlG82Np8rmukZiieWrYNvAZDVztlzq92OhP2EqToOJZ934GDBoDL6YY1VKOBbF4T7jpkYOVktIRMvp8Cp_sBixFI8VviUu1zlBqmguUXX7IPWD613WSSCPghdx4wSJJbQIDD-G-xUlMmipSlQFh91Ul8GEJ4XwBcgUx8SLou7vjEDd73pacH-pyzE36-W9BKM3EKX9wdXWC1xLJhpita4TOPSk_1rnRTvOyFd1D61xRihodESeUHNyWEfeEfIyzrwpXUYCdnUg2oeaNbrjNwuDxpCc1sLnPaa6E1g8H9PlQMaAaNTmwbyyQAAAAF27bvsAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
