#!/usr/bin/env python

import os
import tweepy
import yaml

CONFIG_FILE = os.path.expanduser('~/.twaggr.yaml')

if not os.path.exists(CONFIG_FILE):
    raise IOError(u'Configuration file does not exist at %s, please create one'
                  % CONFIG_FILE)

config = yaml.load(open(CONFIG_FILE))
auth_config = config['auth']
rules_config = config['rules']

# Mandatory parameters
CONSUMER_KEY = auth_config['CONSUMER_KEY']
CONSUMER_SECRET = auth_config['CONSUMER_SECRET']
ACCESS_TOKEN = auth_config['ACCESS_TOKEN']
ACCESS_SECRET = auth_config['ACCESS_SECRET']
MEMBERS_LIST = rules_config['MEMBERS_LIST']

# Optional parameters
HASHTAG = rules_config.get('HASHTAG')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def to_be_retweeted(tweet):
    rules = [tweet.retweeted is False]
    if HASHTAG:
        rules.append(HASHTAG in tweet.text)
    return all(rules)

try:
    crew = filter(lambda l: l.name == MEMBERS_LIST, api.lists())[0]
except IndexError:
    raise RuntimeError(u'Members list not found: %s' % MEMBERS_LIST)

for tweet in filter(to_be_retweeted, crew.timeline(count=100)):
    print u"Found a tweet to retweet: %s" % tweet.text
    tweet.retweet()
