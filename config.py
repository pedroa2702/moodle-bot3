import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = os.environ.get(int("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")


# DATOS DEL MOODLE
USUARIO = os.environ.get("USUARIO_MOODLE", "")
PASSWORD = os.environ.get("PASSW_MOODLE", "")
USUARIO_ID = os.environ.get(int("ID_MOODLE", ""))
ZIP_MB = os.environ.get(int("TAMANO_ZIP", ""))
MOODLE_URL = os.environ.get("MOODLE_URL", "")



OWNER = os.environ.get(int("ID_TELEGRAM", ""))
