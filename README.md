# Twaggr

Twaggr is a (very) simple tweet aggregator. It looks for tweets matching a given pattern from one of your lists and retweets them automatically.

**/!\ this is work in progress, don't use it (yet).**

## Use case

You have a company, an association or a user group account and want it to retweet tweets from any team member matching a given pattern, eg. containing a particular hashtag, automatically. Good news, Twaggr may be for you.

## Installation

TODO

## Usage

TODO: explain how to create a twitter app

Sample configuration file in `~/.twaggr.yaml`:

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

TODO: sample crontab entry

## Authors

The [Scopyleft](http://scopyleft.fr/) crew.

## License

MIT licensed.
