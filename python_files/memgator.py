import os
import time
import json

my_file = open("../OutputFiles/uniqueURI.txt", "r")
content = my_file.readlines()
lines = [line.rstrip() for line in content]


for link in lines:
    os.popen("./memgator-darwin-amd64 -f JSON " + link + " > OutputFiles/memento.json")
    time.sleep(15)

    filesize = os.path.getsize("memento.json")

    if filesize == 0:
        print(link + "   " + "mementos: 0")

    else:
        with open("memento.json", "r") as read_file:
            data = json.load(read_file)
            for line in data:
                links = []
                if 'list' in data['mementos']:
                    for link in data['mementos']['list']:
                        links.append(link['datetime'])
                        count = 0
                        for link in links:
                            count += 1
        print(data['original_uri'] + "   " + "mementos: ", count)
