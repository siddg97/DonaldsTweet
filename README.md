# DonaldsTweet
A twitter bot which predicts donald trumps next potential tweet


## APIs Used:
 - __[tweepy](https://github.com/tweepy/tweepy)__ - a python library for the twitter API
 - Documentation can be found __[here](./tweepy.pdf)__ !
 
## Setup for API:
 - `pip3 install tweepy` - For python 3 and up
 - `pip install tweepy` - For python 2 and under
  #### NOTE: 
  - We assume you have installed `pip3` or `pip` before hand on your device.
  - Alternatively you could clone the `tweepy` repository from GitHub:
    ```
      git clone https;//github.com/tweepy/tweepy.git
      cd tweepy
      python setup.py install
    ```
   - You will need to go [here](apps.twitter.com) to get credentials requiered for your bot!
   
   
## Usage of the API :
    
   `import tweepy`
    
## Credentials Required :
  - __Consumer Key__
  - __Consumer Secret__
  - __Access Token__
  - __Access Token Secret__
  
  #### Authenticating Developer Account with `tweepy` 
 
 - Initialize your credentials:
    ```
    consumer_key = 'consumer key'
    consumer_secret = 'consumer secret'
    access_token = 'access token'
    access_token_secret = 'access token secret'
    ```
  - Authentication:
    ```
    auth = tweepy.OAuthHandler(consumer_key, consumer_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    ```

## Functionality of the Bot :
 - At the moment __DonaldsTweet__ tweeets a potential tweet which is generated based on the last 100 tweets from Donal Trump

## Tweet Generation Model :
 - We use the `Markov Chain Model` with a history of 2 words and make a markov tree based on the inputs.
 - To generate a random tweet we select a random path from the root of the tree to the end, giving us a grammatically correct tweet.

## A project by :
> ### Clara Hong
> ###     &
> ### Siddharth Gupta

