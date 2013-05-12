import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    #ntweets = lines(tweet_file)

    giantDict = {}

    count = 0

    for l in tweet_file:
        #print l
        d = json.loads(l)
        if d.has_key('text'):
            tweet = d['text']
            for w in tweet.split():
                count += 1
                w = w.lower() #make lowercase so it can match
                if giantDict.has_key(w):
                    giantDict[w] += 1
                else:
                    giantDict[w] = 1
                   
    for w,n in giantDict.iteritems():
        print w, float(n)/count


    #print nlookup, ntweets

if __name__ == '__main__':
    main()
