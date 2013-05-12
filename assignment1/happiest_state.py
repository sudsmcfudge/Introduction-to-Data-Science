import sys
import json
import types

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

def getScore(tw,lookup):
    score = 0
    for w in tw.split():
        #print w
        w = w.lower() #make lowercase so it can match
        if lookup.has_key(w):
            score = score + lookup[w]
    return score

#def getState(tw):
#    st = ''
#
#    if tw.has_key('place'):
#        if tw['place'] is types.DictType:
#            s = tw['place']['full_name']
#            if len(s) >= 2:
#                st = s[-2:]
#
#    return st

STATES = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def getState(tw):
    st = ''

    if tw.has_key('user'):
        u = tw['user']
    else:
        return st

    if 'en' not in u['lang']:
        return st

    #print u['location']

    loc = u['location']
    
    # first case:
    # check to see location of form: CITY, ST
    s = loc.split(',')
    if len(s) == 2:
        #print loc
        abv = s[1].strip()
        if len(abv) == 2: # easy one
            st = abv.upper()
            return st
         
    # second case:
    # look for full state names
    lower_loc = loc.lower()
    for abv,state in STATES.iteritems():
        #print abv, state
        if lower_loc.find(state.lower()) > 0:
            #print loc
            st = abv
            return st


    return st
        

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentDict = mkdict(sent_file)    

    stateDict = {
        'AK': 0,
        'AL': 0,
        'AR': 0,
        'AS': 0,
        'AZ': 0,
        'CA': 0,
        'CO': 0,
        'CT': 0,
        'DC': 0,
        'DE': 0,
        'FL': 0,
        'GA': 0,
        'GU': 0,
        'HI': 0,
        'IA': 0,
        'ID': 0,
        'IL': 0,
        'IN': 0,
        'KS': 0,
        'KY': 0,
        'LA': 0,
        'MA': 0,
        'MD': 0,
        'ME': 0,
        'MI': 0,
        'MN': 0,
        'MO': 0,
        'MP': 0,
        'MS': 0,
        'MT': 0,
        'NA': 0,
        'NC': 0,
        'ND': 0,
        'NE': 0,
        'NH': 0,
        'NJ': 0,
        'NM': 0,
        'NV': 0,
        'NY': 0,
        'OH': 0,
        'OK': 0,
        'OR': 0,
        'PA': 0,
        'PR': 0,
        'RI': 0,
        'SC': 0,
        'SD': 0,
        'TN': 0,
        'TX': 0,
        'UT': 0,
        'VA': 0,
        'VI': 0,
        'VT': 0,
        'WA': 0,
        'WI': 0,
        'WV': 0,
        'WY': 0
}



    for l in tweet_file:
        #print l
        d = json.loads(l)
        state = getState(d)
        if d.has_key('text') and (state != ''):
            tweet = d['text']
            #print tweet
            score =  getScore(tweet, sentDict)

            if stateDict.has_key(state): #if abv is actually a state
                stateDict[state] += score

    d_sorted = sorted(stateDict.iteritems(), key=lambda x: x[1], reverse=True)

    st, v = d_sorted[0]
    #print d_sorted
    
    print st

if __name__ == '__main__':
    main()
