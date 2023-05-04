import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "13764765")) #optional
API_HASH = getenv("API_HASH", "0255274ce6771d5535c201dd05ce8d79") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6139027175").split()))
OWNER_ID = int(getenv("OWNER_ID", "6290258924"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://techbrou:pandey2120@cluster0.oog5hnb.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6288784069:AAFNIMutl1UjKNh9Tegp7POUWk2PRV3_Uk8")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/a11b92d11d3b9ab8e77ee.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "UTKARSH")
PM_LOGGER = getenv("PM_LOGGER", "727610771")
LOG_GROUP = getenv("LOG_GROUP", "972249333")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/utkarshrobin/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkANJYSr8I40Q5z_NupOyrK3AjkkxFePHlvsxKI7dLhr0pCLqLMLlqP3fbytt1lzGcOfGQk43_IFhA6Py8xaYZqkoXdWawJZv3Ud6vIAV5rYftJ1wE-xaJIG3zG3PrIrnwM7ye9iT2xjrQAZIfTI1sIHCxsnBOOMW0ubzBF9j0aVWN7y6pI37_4DBMTWxhVFlpX6R_q1IrudUGB5CFJ6C69tLI-FoandkUdIXXsvvAZOatlmW1hi9q4IkMMKakl6QX44MoNLMN_uj_g80wnJ4A0jkgSA_CKKs4BPUs0y6KS982tkOY1ZSKnrWqpyEo4qf2Fxijzc40JvioX19L0YUxjfAAAAAF27bvsAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
