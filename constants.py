import json

from decouple import config

TOKEN = config('TOKEN')
OWNER = config('OWNER')

with open('labels.json') as json_file:
    LABELS = json.load(json_file)
