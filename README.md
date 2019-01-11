# Mensabot2 (Slack)

This is a simple bot made to be run by a cronjob, using Slack Webhooks to send the meal offers of the Mensa.


## Requirements

For running the thing manually you will need
- Python (>=3.6);
- the *requests* package (`pip install -r requirements.txt`).

Alternatively you can use Docker.

## Usage

### Manually

1. Set the `SLACK_URL` and openmensa constants accordingly.
2. Run `python3 bot.py` with a cronjob at the time of your wish.

### Docker

1. Build with `docker build -t eightsq/mensabot .`.
2. Create container using `docker create ...`, specifying `SLACK_WEBHOOK`, `OPENMENSA_MENSAID` and `MENSA_URL` environment variables. You can also modify the label `cron.schedule` if you have a docker cron runner.
3. Start the container (`docker start`) via a cronjob (or using a docker cron runner).

## Roadmap

- Containerization
	- Configuration over environment variables
