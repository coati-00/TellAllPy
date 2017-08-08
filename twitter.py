import json
import sys

from PyQt5.QtWidgets import QApplication, QWidget
import tweepy


with open('config.json', 'r') as twitter_config:
    config = json.load(twitter_config)


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def other_main():
  # took this code from an example will take care of redundancy later
  cfg = {
    "consumer_key"        : config["consumer_api_key"],
    "consumer_secret"     : config["consumer_secret"],
    "access_token"        : config["access_token"],
    "access_token_secret" : config["access_token_secret"]
    }

  api = get_api(cfg)
  #tweet = "Test the bot!"
  #status = api.update_status(status=tweet)


if __name__ == '__main__':
  app = QApplication(sys.argv)

  w = QWidget()
  w.resize(450, 450)
  w.move(300, 300)
  w.setWindowTitle('TellAllPy')
  w.show()

  sys.exit(app.exec_())