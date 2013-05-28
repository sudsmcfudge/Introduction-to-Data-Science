from myMapper import Mapper
from myReducer import Reducer

import json

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for line in data:
            mapper(self, line)

        for key in self.intermediate:
            reducer(self, key, self.intermediate[key])

        #jenc = json.JSONEncoder(encoding='latin-1')
        jenc = json.JSONEncoder()
        for item in self.result:
            print jenc.encode(item)

def main():
    poker = MapReduce()
    
    fp = open('hands.dat')

    poker.execute(fp,Mapper,Reducer)

    fp.close()

if __name__ == '__main__':
    main()
