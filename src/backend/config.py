import os

DEBUG = False
SERVER_NAME=os.environ.get("PORT", "localhost:8000")
LOGGER_HANDLER_POLICY='production'