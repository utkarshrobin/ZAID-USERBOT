import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "23965007")) #optional
API_HASH = getenv("API_HASH", "128d2a36a2aaceec5f9daa257a0eb6e3") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5379811679").split()))
OWNER_ID = int(getenv("OWNER_ID", "609517172"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://techbrou:Pandey2120@cluster1.6ujsngj.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6997586009:AAH5lUk0GWxjXoLQvBMYlzyN2BqAMIeu1nk")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/a11b92d11d3b9ab8e77ee.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "UTKARSH")
PM_LOGGER = getenv("PM_LOGGER", "727610771")
LOG_GROUP = getenv("LOG_GROUP", "972249333")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/utkarshrobin/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
STRING_SESSION1 = getenv("STRING_SESSION1", "BQDNvmIAElLxeofjh8HjVuI-oY4MjL-CSKF89hlH0T7YAX5-k8afF50wyLpf_cUHhkp7mtmIA16qVtnuxs1-7kVMO94cjvNUo3BXsJMNSkkno5NWrH0MBNnjgt_azLf59E3nn5RgmKkCzZ7gWugTr25Upd7V8rsx7r2LT87VWW8UxXwNIVT09gky9x9w0e2WQA2CAOwPzF7LMtZsKJa548IkGQ9lGhN6fbmzxBDwrlXPpKl6LUwnhMMFjvuk3CBdjkNB-tD2qD3tJKewSByEzs7e76wvrCqbzL5zUT42vfYB_v3drtzY76-SbiaNnkTiCKpVvdAuq-AjRYUh--N9cJ-ECJKyCgAAAAGxjNB6AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
