import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "11834917")) #optional
API_HASH = getenv("API_HASH", "be32c8041eaad8d3590071da14bab91b") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6139027175").split()))
OWNER_ID = int(getenv("OWNER_ID", "6104126188"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://techbrou:pandey2120@cluster0.oog5hnb.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6016553840:AAGshFLMai35LW1mmMqxo0qdc1kPgBMHkPY")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/a11b92d11d3b9ab8e77ee.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "UTKARSH")
PM_LOGGER = getenv("PM_LOGGER", "727610771")
LOG_GROUP = getenv("LOG_GROUP", "972249333")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/utkarshrobin/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
STRING_SESSION1 = getenv("STRING_SESSION1", "BQCcYO4Aso9CXO47-VbFtLa2tH7LUD2MWMQ7jnUJLVUpF9N8bD-f_HK8qW9ei7gRVYljrN1jPK-KssIQLiBe6pbhkrteafuEQuKUbgQblwfgPwmGHhD8t7NZY663D1lDBpivv9ZWXtSkstZZl1IeOjKpb_BPOdH1YmmPiDGqtiWTSXCk-AlT5jTx_qmhWUgW5hrIOx9WjidVqEaiW0cihJnFBfocXiJPvhR1tlPAculZmWfFngVPtDPIEMSJQ0cJ2uJoiGHqKzs6CgXP-9hSXtoFGZ1iFTavJbVPKCmdLHrmvzyesJJL5__D02fwqjgqtJEf_vfFk5zyIB273WUTOOXeusYqMgAAAAFr1ZLsAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
