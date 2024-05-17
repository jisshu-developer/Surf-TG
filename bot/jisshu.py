from os import getenv

class Telegramm:
   AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL").split(",")]
   ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "surfTG")
   THEME = getenv("THEME", "quartz").lower()
