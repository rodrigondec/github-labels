import json

from decouple import config

TOKEN = config('TOKEN')
OWNER = config('ORG')
REPO = config('REPO')

with open('labels.json') as json_file:
    LABELS = json.load(json_file)
