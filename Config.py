import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "20470794")
    API_HASH = os.environ.get("API_HASH", "a1397a2838ad7e410a78ff2d87aab206")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", ,"6829224186:AAHUoLwJb1oFE4t8Xm7jctxvVVOt_T4KJ-0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLgBu60TkUeD45QaiUnxYuFPK1rM29qjKb7bxKVpJodFsGR63_VPqXdYOr9hUFoD_pAJ10tMCkEOrxARpUIb4leHIkl6nkqHxqTcQKec983WBBIWAoThfi_zHQ05IbSkPWDD-ryxTnkri9XzJGrPc0lUiw3m0xlBD_5JYIJ3AWGk4Xk9-idX9UJgSA7KtZN9gT5ChKlYoWtyMIjFxQGmnad-eW5s0j6a-cIdWILwC084FmIQypNgqjh4jCW7-zWCBOuFzJCdMadlk4UkMlluPvBMszjMKSK6RRd17mham_f9N1ffNSgKfu45lyd_21K88V-KzSQCrAFwSZY8iw9HjRA-_cQ=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ShaankaraSvaraBot")
    OWNER = os.environ.get("OWNER", "Vedadhyayi") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Lokshankaram") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d6374a94e6de63dbb37b.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/1aeabeee03b9a52f0b1b3.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "7495539739")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "86400")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
