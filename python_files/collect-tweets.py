import sys
import json
from twarc import Twarc2, expansions
from configparser import ConfigParser

# CHANGE THIS TO YOUR TWARC CONFIG
TWARC_CONFIG_FILE = "<path_to_tawarc_config>"
OUTPUT_FILE = "../OutputFiles/tweets.jsonl"  # line-oriented JSON
MAX_TWEETS = 100

# read Twitter API keys from twarc config file, setup twarc2 object
config = ConfigParser(interpolation=None)
with open(TWARC_CONFIG_FILE) as twarc_config:
     config.read_string("[TWARC]\n" + twarc_config.read())
bearer_token = config['TWARC']['bearer_token'].strip('\'')
t = Twarc2(bearer_token=bearer_token)

# use covid as default search term unless one provided
search_term = "covid"
if len(sys.argv) > 1:
     search_term = str(sys.argv[1])

# limit search results to English language, with links, and no retweets
query = search_term + " lang:en has:links -is:retweet"

search_results = t.search_recent(query=query, max_results=MAX_TWEETS)

num_tweets = 0
for page in search_results:
     result = expansions.flatten(page)
   
     # open the file and write one JSON object per new line (jsonl format)
     with open(OUTPUT_FILE, 'a') as filehandle:   # if you want to append, change 'w' to 'a+'
          for tweet in result:
               filehandle.write('%s\n' % json.dumps(tweet))
               num_tweets = num_tweets + 1
               if num_tweets == MAX_TWEETS:
                    # must include this to stop after a certain # of tweets
                    search_results.close()

print(num_tweets, "tweets written to " + OUTPUT_FILE + " for query \"" + query + "\"\n");
