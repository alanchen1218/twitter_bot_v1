# containerize the app

# base image, contains Python3.7 and pi
FROM python:3.7-alpine 

COPY bots/config.py /bots/
COPY bots/favretweet.py /bots/
# COPY bots/followFollowers.py /bots/
# COPY bots/autoreply.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "favretweet.py"] 

# commands to run after it's deployed
# docker build . -t fav-retweet-bot

#  docker run -it -e CONSUMER_KEY="<consumer key>" \
# -e CONSUMER_SECRET="<consumer secret>" \
# -e ACCESS_TOKEN="<access token>" \
# -e ACCESS_TOKEN_SECRET="<access token secret>" \
# fav-retweet-bot