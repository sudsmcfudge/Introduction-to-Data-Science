# Python Reducer() : key is a made hand, e.g. 'flush' .
# Count up how many unique hands make e.g. a flush.
def Reducer(jsmr_context, key, arr): 
  mysum = len(arr)

  output_str = '%s:%d' % (key, mysum) 
  jsmr_context.emit(output_str) 
