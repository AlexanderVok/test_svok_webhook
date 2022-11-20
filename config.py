import hashlib
import os

API_TOKEN = os.getenv("API_TOKEN")

# webhook settings
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
WEBHOOK_PATH = f'/test_assistants_bot/' + hashlib.sha256(API_TOKEN.encode('utf-8')).hexdigest()
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
# WEBAPP_HOST = 'localhost'  # or ip
# WEBAPP_PORT = 8080

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)