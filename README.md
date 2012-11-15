# Twaggr

Twaggr is a (very) simple tweet aggregator. It looks for tweets matching a given pattern from one of your lists and retweets them automatically.

**/!\ this is work in progress, don't use it (yet).**

## Use case

You have a company, an association or a user group account and want it to retweet tweets from any team member matching a given pattern, eg. containing a particular hashtag, automatically. Good news, Twaggr may be for you.

## Installation

```
$ git clone https://github.com/scopyleft/twaggr.git && cd twaggr
$ virtualenv --no-site-packages `pwd`/env/bin
$ source env/bin/activate
$ pip install requirements.txt
```

## Usage

First you'll have to register a new twitter app at [Twitter Dev Center](https://dev.twitter.com/apps/new). This will get you a `CONSUMER_KEY` and `CONSUMER_SECRET`.

__Note:__ Please set the app to ask for read + write access.

Then you'll need to authorize the app you've just created for your twitter user:

```
>>> import tweepy
>>> auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
>>> auth.get_authorization_url()
```

That last command will print an authorization url you'll have to open in your Web browser. Copy the PIN number provides once you've authorized the app to access your twitter account, and get back to your Python prompt:

```
>>> auth.get_access_token('<paste PIN number here>')
>>> auth.access_token.key    # that will be you ACCESS_TOKEN
>>> auth.access_token.secret # that will be you ACCESS_SECRET
```

You can now create the twaggr configuration file in `~/.twaggr.yaml`:

```yaml
auth:
    CONSUMER_KEY:    "<your twitter app consumer key>"
    CONSUMER_SECRET: "<your twitter app consumer secret>"
    ACCESS_TOKEN:    "<your twitter access token>"
    ACCESS_SECRET:   "<your twitter access secret>"
rules:
    HASHTAG:         "#scopyleft"
    MEMBERS_LIST:    "Scopycrew"
```

Run:

```
$ python twaggr.py
```

Now you may add some [crontab](http://en.wikipedia.org/wiki/Crontab) entry:

```
*/5 * * * * /home/user/twaggr/env/bin/python /home/user/twaggr/twaggr.py >> ~/twaggr/twaggr.log
```

That will run the script every five minutes and log the output in a `~/twaggr/twaggr.log` file.

## Authors

The [Scopyleft](http://scopyleft.fr/) crew.

## License

MIT licensed.
