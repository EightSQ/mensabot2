FROM python:3.7-alpine

LABEL	maintainer="EightSQ <ok@electronvolt>" \
		description="The slack-mensabot" \
		version="1.0" \
		cron.schedule="45 9 * * 1-5"

ENV	OPENMENSA_MENSAID=62 \
	MENSA_LINK="https://www.studentenwerk-potsdam.de/mensa-griebnitzsee.html"

WORKDIR /var/src/app

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "bot.py"]
