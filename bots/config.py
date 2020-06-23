import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    # consumer_key = os.getenv("CONSUMER_KEY")
    # consumer_secret = os.getenv("CONSUMER_SECRET")
    # access_token = os.getenv("ACCESS_TOKEN")
    # access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    consumer_key = 'UEyDHQijVRtxshOv0UETIBU8Z'
    consumer_secret = '2ahRHJ4aYLMPetuTwPx4klveO3KE1smI2ySpgtIEQyRgVpJzvi'
    access_token = '1274884429983313920-EvpJXhKPGyAP2YcXKVNf60IsTqRqNM'
    access_token_secret = 'G62PzPrNg0MDXVULqFhl72ErpIPKuyBojN9U82DEvHNSl'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e

    logger.info("API created")
    return api

create_api()