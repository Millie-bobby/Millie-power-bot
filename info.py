import re
from os import environ, getcwd
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from prettyconf import Configuration
from logging import WARNING, getLogger
from prettyconf.loaders import EnvFile, Environment



env_file = f"{getcwd()}/.env"
info = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])

getLogger("pyrogram").setLevel(WARNING)
LOGGER = getLogger(__name__)

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode="html",
            sleep_threshold=60
        )

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://te.legra.ph/file/5b2ec8d541fee97e63037.jpg https://te.legra.ph/file/14cea0c96e38ca47aca1c.jpg https://te.legra.ph/file/dad19fa5c940e89ec74aa.jpg https://te.legra.ph/file/727661d762e4aa3176e06.jpg https://te.legra.ph/file/a3cfa1226dab427486dd7.jpg https://te.legra.ph/file/ba56e6f9bf8f8638a5fb6.jpg https://te.legra.ph/file/24e85054dad2adc145961.jpg https://te.legra.ph/file/cc2842ea31dbeac22e8a5.jpg https://te.legra.ph/file/500ba5fb6ec16b4cabb28.jpg https://te.legra.ph/file/ba003b3cd73cfb7deb697.jpg https://te.legra.ph/file/4cf8d8e436f5a2dec30c1.jpg https://te.legra.ph/file/89249bc2f5b7a4473695b.jpg https://te.legra.ph/file/218b6cf8d19add39b0f19.jpg https://te.legra.ph/file/dd1d29623c4ed084fc2f7.jpg https://te.legra.ph/file/966eea5237847017ae209.jpg https://te.legra.ph/file/78c506103922f06291427.jpg https://te.legra.ph/file/5f07f995260d4036b562e.jpg https://te.legra.ph/file/6a0e9cba9eb2f326a9782.jpg https://te.legra.ph/file/24224bd1cd9524e870033.jpg https://te.legra.ph/file/0d6303364d49cd20612fc.jpg https://te.legra.ph/file/000469af1adb1dc0d4045.jpg https://te.legra.ph/file/614f3f0c080eb81736b15.jpg https://te.legra.ph/file/1b565643d97bd8d6e1f35.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5157282689').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
USE_AS_BOT = environ.get("USE_AS_BOT", True)


# maximum message length in Telegram
MAX_MESSAGE_LENGTH = 4096

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# the maximum number of 'selectable' messages in Telegram
TG_MAX_SELECT_LEN = environ.get("TG_MAX_SELECT_LEN", "100")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

#CommandsOfGroup
ENABLED_LOCALES = environ.get("ENABLED_LOCALES", "en")
BOT_USERNAME = environ.get("BOT_USERNAME", "@Millie_power_robot")
OWNER_ID = environ.get("OWNER_ID", "5157282689")
DEV_USERS = environ.get("DEV_USERS", "5157282689")
SUDO_USERS = environ.get("SUDO_USERS", "5157282689")
BOT_ID = environ.get("BOT_ID", "2127894418")
SUPPORT_STAFF = environ.get("SUPPORT_STAFF", "5157282689")
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "@millie_robot_update")
ENABLED_LOCALES = [str(i) for i in info("ENABLED_LOCALES", default="en").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Millie")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001547941154))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'millie_robot_update')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n???IMDb Data:\n\n???? Title: <a href={url}>{title}</a>\n???? Genres: {genres}\n???? Year: <a href={url}/releaseinfo>{year}</a>\n???? Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "True"), True)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001547941154')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
DELETE_TIME = environ.get('DELETE_TIME', '0')

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two seperate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as diffrent buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your Currect IMDB template is {IMDB_TEMPLATE}"
LOG_STR += ("auto delete is active , bot will be deleting movie results when {DELETE_TIME} \n")
