import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CIRCO_DEFAULT_ROLE = os.getenv('CIRCO_DEFAULT_ROLE')