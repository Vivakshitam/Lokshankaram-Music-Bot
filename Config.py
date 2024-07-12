import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Lokshankaram") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d6374a94e6de63dbb37b.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/1aeabeee03b9a52f0b1b3.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "86400")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
