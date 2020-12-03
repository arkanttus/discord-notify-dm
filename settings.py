import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
DEFAULT_ROLE_GUILD = os.getenv('DEFAULT_ROLE_GUILD')

MEMES_PHRASES = (
    ['guei', 'fdp'],
    [
        'TEU PAI',
        'É TU',
        'TEU TIO',
        'TU Q DEIXA',
        'MACHISTA',
        'QUEM ?',
        'O BIRO LIRO',
        'O BRUNO',
        'TE LASCAR'
    ]
)

ANWSER_MEMES = (
    ['tu', 'é tu', 'eh tu'],
    [
        'TEU PAI',
        'PERGUNTOU ?',
        'TEU TIO',
        'QUEM ?',
        'TE LASCAR',
        'FDP'
    ]
)