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

    def countOccurance(self, word):
        letterCounts = []
        for letter in word:
            letterCounts.append(word.count(letter))
        return letterCounts

    def compare(self, a, b):
        if len(a) != len(b):
            return -1
        misses = 0
        word = []
        for i in range(len(a)):
            if a[i] != b[i]:
                misses += 1
            else:
                word.append(a[i])
        return misses, word

    