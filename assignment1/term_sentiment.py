import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    #print str(len(fp.readlines()))
    return len(fp.readlines())

def mkdict(afinnfile):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
        
    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #nlookup = lines(sent_file)
    #ntweets = lines(tweet_file)
    lookup = mkdict(sent_file)    

    newDict = {} #{key: array([sentSum, ntweets])}

    for l in tweet_file:
        #print l
        score = 0
        d = json.loads(l)
        if d.has_key('text'):
            tweet = d['text']
            #print tweet
            for w in tweet.split():
               #print w
               w = w.lower() #make lowercase so it can match
               if lookup.has_key(w):
                   score = score + lookup[w] #sum score
               elif not newDict.has_key(w): #find new words
                   newDict[w] = [0,0] # initialize new word

            #update scores
            for w in tweet.split():
                w = w.lower()
                if newDict.has_key(w):
                    newDict[w][0] += score
                    newDict[w][1] += 1

    #print newDict.items()

    for w,(s,n) in newDict.iteritems():
        print w.encode('utf-8'), float(s)/n

    #print nlookup, ntweets

if __name__ == '__main__':
    main()
