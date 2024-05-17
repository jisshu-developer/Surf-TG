from os import getenv

class Telegramm:
   ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "zishan")
   THEME = getenv("THEME", "quartz").lower()
