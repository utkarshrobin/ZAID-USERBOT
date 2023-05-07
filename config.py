import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "13764765")) #optional
API_HASH = getenv("API_HASH", "0255274ce6771d5535c201dd05ce8d79") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6158769611").split()))
OWNER_ID = int(getenv("OWNER_ID", "6048922953"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://techbrou:pandey2120@cluster0.oog5hnb.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6139945042:AAGMb8-bQKsH_-5pmXClt8ZrUhMg3_fFalc")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/a11b92d11d3b9ab8e77ee.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "UTKARSH")
PM_LOGGER = getenv("PM_LOGGER", "727610771")
LOG_GROUP = getenv("LOG_GROUP", "972249333")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
STRING_SESSION1 = getenv("STRING_SESSION1", "BQDSCJ0AqR2kEjVJBvjXzxMJyulEtX6n7fgiq03zqoabYfa62ciiG2gQ6vweGpYeisccBXCW1PdAWp9ifC03aG34L1lHGQrFwW4-FMTMDav7jG1jepyWC2aKHvD2_13YtjWefWoC7GWFyvmSXFfUQPSEZRDGWpQ7leeH0fzPViWGVXZrEwTHE6q4J6gqiNWMrkox9EF_FEyw1MB6p14vybW0KRPobdjzQMmrgGxDUbUi3UDFGL3ZuPg-JJ0xOYZ8OwG8HMqRwBTir0MH13Lt1cE4tuQhx3DXrFlsdmKQ42gfv5HYm1ewLjQ73fv7reNOmSJTMJMbcDBsP3qRMO0kvbxqfTyJKgAAAAFoiz1JAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
