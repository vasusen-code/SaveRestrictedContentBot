FROM encodev/srcbot:latest
WORKDIR /usr/src/app
COPY . .
RUN rm -rf .git Dockerfile
CMD ["bash", "srcbot.sh"]
