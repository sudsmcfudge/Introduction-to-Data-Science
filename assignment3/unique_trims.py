import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: id
    # value: string of nucliotides
    key = record[0]
    value = record[1]
    mr.emit_intermediate(value[:-10],1)

def reducer(key, list_of_values):
    # key: id
    # value: string of nucliotides missing last 10 chars
    
    #printing only the keys removes duplicates
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
