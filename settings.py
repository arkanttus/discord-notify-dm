import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
DEFAULT_ROLE_GUILD = os.getenv('DEFAULT_ROLE_GUILD')