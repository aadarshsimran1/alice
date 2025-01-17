import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 23362564
API_HASH = "0471f0a3149c315823c77eef2519ad8d"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8136136736:AAGk1HK8zF2jGLwPO3ljztVmfn27xCg5VsQ"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://aadarshsimran19:aadarshsimran19@cluster0.et6rm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002117754451

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 911244769

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/techno_aadarsh19"
SUPPORT_GROUP = "https://t.me/techno_aadarsh19"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFkfAQAUm-jp4RYQ28zhF2B20MqP2qZ_J19bDEoYEhkPXHRvcw6aK7_m4GZE-RPQ4AMJWMdHMh42gUy04sedws6ohEAtn_eaJveOrfvJjgZRimAvLpeXgUlTG2NeBQ7T-1nXjuychC83OewhJEwr7UnkEAKCKoPJzji-hcpsh4YO60lOxyeidVWOKabFPY1sx2Xy5kVH_JrhNvHHMW2QMNSUlPq4grwkXO7WUmnj4prXsoJqXfbAy7Ehw7vQI_rAFd7092DiNHfsWwSTBMWMHokafnsSTgyugpJAvLGBWKqp49uPSf-SsW9BKcPhVVADNnbUXzXQ25PnNl_NHFG5tNYVT631gAAAAHXXHYfAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/vTelegraphBot-01-17-35"

PING_IMG_URL = "https://graph.org/vTelegraphBot-01-17-35"

PLAYLIST_IMG_URL = "https://graph.org/vTelegraphBot-01-17-35"
STATS_IMG_URL = "https://graph.org/vTelegraphBot-01-17-35"
TELEGRAM_AUDIO_URL = "https://graph.org/vTelegraphBot-01-17-35"
TELEGRAM_VIDEO_URL = "https://graph.org/vTelegraphBot-01-17-35"
STREAM_IMG_URL = "https://graph.org/vTelegraphBot-01-17-35"
SOUNCLOUD_IMG_URL = "https://graph.org/vTelegraphBot-01-17-35"
YOUTUBE_IMG_URL = "https://graph.org/vTelegraphBot-01-17-35"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/vTelegraphBot-01-17-35"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/vTelegraphBot-01-17-35"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/vTelegraphBot-01-17-35"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
