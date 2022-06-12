## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQArUVe7SznVjge9u2EhV_hmvMUzvYvk5w_b64V_1uqp629_W8YhK2ratpM1w4Eh4gpUuzM-Tg02DHaSpT23QC5TuJntt7aBB1UzgJ5HbonWZCo2M3Lzs4Z2YrpdIZdxSNqOx0UcUKiWHFLElc7rVmOmuAzlGBUFhcA7MNv6AE_nW_Z8HiRn_U2Hw9WNVwybw5rdKiXoujZDyr5Vdizxr-E4bTrq7r4Lnt-wbMcePY6xQTWdtA2KBGH0kWKzhhczX7PPerJ4Vf509l4R421Dg0qz7hdj6C07d2B-PhNygLkCPnuM7RKALbLSgYSh8bZ04i9Og_MdB4Kh902vdKLRh88NAAAAATBzenwA")
BOT_TOKEN = getenv("BOT_TOKEN", "5544122497:AAG8dFeQamWYTG0e7dgYmFOE9kt0-6RKT_4")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "sam")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ls_1s")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "HS87YBOT")
OWNER_ID = getenv("OWNER_ID", "1932268093")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXYXQ")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "lRlRIRl")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "eceoo")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1932268093").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
