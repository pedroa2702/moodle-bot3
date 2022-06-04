import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")


# DATOS DEL MOODLE
USUARIO = os.environ.get("USUARIO_MOODLE", "")
PASSWORD = os.environ.get("PASSW_MOODLE", "")
USUARIO_ID = os.environ.get("ID_MOODLE", "")
ZIP_MB = int(os.environ.get('TAMANO_ZIP', '300'))
MOODLE_URL = os.environ.get("MOODLE_URL", "")
OWNER = [1051187422]
