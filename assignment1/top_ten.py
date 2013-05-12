import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    #ntweets = lines(tweet_file)

    hashDict = {}

    count = 0

    for l in tweet_file:
        #print l
        d = json.loads(l)
        if d.has_key('entities'):
            entities = d['entities']
            for h in entities['hashtags']:
                tag = h['text']
                if hashDict.has_key(tag):
                    hashDict[tag] += 1
                else:
                    hashDict[tag] = 1
        
    d_sorted = sorted(hashDict.iteritems(), key=lambda x: x[1], reverse=True)

    for w,n in d_sorted[:10]:
        print w, float(n)


if __name__ == '__main__':
    main()
