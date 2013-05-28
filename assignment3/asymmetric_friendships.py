import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value) #add it twice
    mr.emit_intermediate(value,key)

def reducer(key, list_of_values):
    # key: person
    # value: list of friends
    for f in list_of_values:
        if list_of_values.count(f) < 2:
            mr.emit((key, f))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
