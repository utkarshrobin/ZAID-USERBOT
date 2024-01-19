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
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGMcpgAtM5zXYl1N8tt27dMZ7lvtKjhS3OFyEwArB-DixE9vfvDLRTUceunsmguNeRZj0uvE35HswtqcxzwyJsEuoXPugckdygJnc0M7QT2ACjVCqIauHM_1zjSccTRuROfHngepDhWcAEKJ_uSh5HiYgDD5OaCdF1Pkb81CDcclFf_Gl80PSPakYCT-pj66koFLpu8WQBqmLqY9i9slA4iXIFKu9j0nUld26WHNwgpCMDaRTk_UpB4RPQ-FmqXjID7DHTkLkq0Lx0SEaavIed9i2WPypgO9UqmsEn-vkn-6pJYJ1KVL3OvepZf8jx-YnLxwpa_CN3bfCD3eE0m-tmtVQJxlQAAAAGR7zBDAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
