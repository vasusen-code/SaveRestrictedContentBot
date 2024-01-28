FROM encodev/srcbot:latest
WORKDIR /usr/src/app
COPY .env .
CMD ["bash", "srcbot.sh"]
