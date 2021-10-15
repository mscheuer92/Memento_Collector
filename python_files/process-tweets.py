import sys
import json

lines = sys.stdin.readlines()  # read in all the lines
for line in lines:
    tweet_data = json.loads(line)  # each line is JSON
    links = []
    if 'urls' in tweet_data['entities']:
        for link in tweet_data['entities']['urls']:
            links.append(link['expanded_url'])
            for link in links:
                # Exclude links from twitter domain, YouTube, and WhatsApp
                if not link.startswith("https://twitter.com") and not link.startswith("https://youtu.be"):
                    print(" " + link)

