import json
import sys

from PyQt5.QtWidgets import QApplication, QWidget
import tweepy


with open('feathered_twitter_config.json', 'r') as feathered_twitter_config:
    feathered_config = json.load(feathered_twitter_config)


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def post_to_feathered_twitter():
    # took this code from an example will take care of redundancy later
    cfg = {
      "consumer_key"        : feathered_config["consumer_api_key"],
      "consumer_secret"     : feathered_config["consumer_secret"],
      "access_token"        : feathered_config["access_token"],
      "access_token_secret" : feathered_config["access_token_secret"]
    }

    api = get_api(cfg)
    #tweet = "Test the bot!"
    #status = api.update_status(status=tweet)


with open('coati_twitter_config.json', 'r') as coati_twitter_config:
    coati_config = json.load(coati_twitter_config)

def post_to_coati_twitter():
    # took this code from an example will take care of redundancy later
    cfg = {
        "consumer_key"        : coati_config["consumer_api_key"],
        "consumer_secret"     : coati_config["consumer_secret"],
        "access_token"        : coati_config["access_token"],
        "access_token_secret" : coati_config["access_token_secret"]
    }

    api = get_api(cfg)
    #tweet = "Test the bot!"
    #status = api.update_status(status=tweet)



if __name__ == '__main__':
    #  post_to_coati_twitter()
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(450, 450)
    w.move(300, 300)
    w.setWindowTitle('TellAllPy')
    w.show()

    sys.exit(app.exec_())