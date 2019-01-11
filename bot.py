#!/usr/bin/python3.7

""" Made with ♥ by EightSQ (2019) """

import sys
import requests
import datetime
import locale

OPENMENSA_MENSAID = 62
SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'
MENSA_LINK = 'https://www.studentenwerk-potsdam.de/mensa-griebnitzsee.html'

date = datetime.date.today().isoformat()
locale.setlocale(locale.LC_TIME, "de_DE")

r = requests.get(f'https://openmensa.org/api/v2/canteens/{OPENMENSA_MENSAID}/days/{date}/meals')
if r.status_code != 200:
    print('failed to load mensa data', file=sys.stderr)
    exit(1)
data = r.json()

payload = {}

payload["text"] = f'Speiseplan für {datetime.date.today().strftime("%A, den %d. %B %Y")}: <{MENSA_LINK}|Online anzeigen>'

payload["attachments"] = []
payload["attachments"].append({})
payload["attachments"][0]["fallback"] = "Heutiges Angebot"
payload["attachments"][0]["color"] = "#46a64f"
payload["attachments"][0]["fields"] = []

for meal in data:
    _meal = {}
    hint = ''
    try:
        if meal["notes"]:
            for note in meal["notes"]:
                if note == 'Schweinefleisch':
                    hint += ':pig2:'
                elif note == 'Rindfleisch':
                    hint += ':cow2:'
                elif note == 'Fisch':
                    hint += ':fish:'
                elif note == 'Gefluegel':
                    hint += ':chicken:'
                elif note == 'Vegan':
                    hint += ':seedling:'
                elif note == 'Vegetarisch':
                    hint += ':seedling::glass_of_milk:'
                elif note == 'Alkohol':
                    hint += ':wine_glass:'
            if hint != '':
                hint = f' {hint}'
    except:
        pass
    _meal["title"] = meal["category"]+hint
    _meal["value"] = meal["name"]
    _meal["short"] = False
    payload["attachments"][0]["fields"].append(_meal)

r = requests.post(SLACK_WEBHOOK, json=payload)
if r.status_code != 200:
    print(f'msg to slack unsuccessful: {r.status_code}', file=sys.stderr)
    exit(1)

