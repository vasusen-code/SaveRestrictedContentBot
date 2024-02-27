FROM encodev/srcbot:2024.02.26
WORKDIR /usr/src/app
COPY .env .
CMD ["bash", "srcbot.sh"]
