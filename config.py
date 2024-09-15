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
BOT_TOKEN = getenv("BOT_TOKEN", "7511209237:AAFTvDsljPOACjgqN-vqVfIlE-_I7GTP058")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/a11b92d11d3b9ab8e77ee.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "UTKARSH")
PM_LOGGER = getenv("PM_LOGGER", "727610771")
LOG_GROUP = getenv("LOG_GROUP", "-1002207135159")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/utkarshrobin/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
STRING_SESSION1 = getenv("STRING_SESSION1", "BQFtrU8AkBCVgOCDTY6YZeMhyPqEIO3kwZoimod-fx4AuceUcpQxb3e8q8-qEgetFZPKbw9Wsih8uDxfSJEGDA44Opss5M-677Kl0BTocurlCtwf3J-YJnbQ0YDNS0HuHdtH8RE2Cycv0jkv4hXXZIQKcSCWfMrS_yvzkzzRmyWN7V8AND5OT-DwVg6R8GzXwLqc5JGBMWWpKWpPxfxR-5_ywm9SJldnCHbeSdP5TM84a0rKYMn3huqRgTZW2PfYoX3uj76Ro_uzo2893JnXYcvx8mvJ_Z2Ria7YuarOrFdTsY00MoIh6B8y9BVVucFhLgVAsfM3ipgLkzabmpMIwF7sJOwwNAAAAAGNCWSSA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
