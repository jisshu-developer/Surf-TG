from os import getenv

class Telegramm:
   AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL").split("-1002107792448, -1001942980809")]
   ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "zkhan111@")
   THEME = getenv("THEME", "quartz").lower()
