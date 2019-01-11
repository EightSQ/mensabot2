# Mensabot2 (Slack)

This is a simple bot made to be run by a cronjob, using Slack Webhooks to send the meal offers of the Mensa.


## Requirements

- Python (>=3.6)
- the *requests* package (`pip install -r requirements.txt`)

## Usage

1. Set the `SLACK_URL` and openmensa constants accordingly.
2. Run `python3 bot.py` with a cronjob at the time of your wish.

## Roadmap

- Containerization
	- Configuration over environment variables
