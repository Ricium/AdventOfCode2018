class functions(object):
    """All the methods one could need"""
    def hello(self, world):
        print('Hello ' + world)
    
    def read(self, path, delim):
        data = open(path, "r")
        return data.read().split(delim)

    def read_integers(self, filename):
        with open(filename) as f:
            return [int(x) for x in f]