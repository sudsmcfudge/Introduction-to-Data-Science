#!/usr/bin/env python

import urllib
import json

for p in range(1,11):
    response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page="+str(p))
    d = json.load(response)
    arr = d["results"]
    
    for tweet in arr:
        if (tweet["iso_language_code"] == "en"):
            print tweet["text"]

    #    for i in range(10):
    #        print arr[i]["text"]

