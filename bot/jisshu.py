from os import getenv

class Telegramm:
   ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "zkhan111@")
   THEME = getenv("THEME", "quartz").lower()
