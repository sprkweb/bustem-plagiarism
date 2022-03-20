# https://en.wikipedia.org/wiki/N-gram
class NGramsGenerator:
    def __init__(self, n=1):
        self.n = n

    # Generate an array of n-grams from an array of tokens (e.g. words)
    def generate(self, tokens: list) -> list:
        if self.n == 1:
            return tokens
        ngrams_number = len(tokens) + 1 - self.n
        if ngrams_number < 1:
            return []
        return [' '.join(tokens[i:i+self.n]) for i in range(ngrams_number)]

    # Generate a dict of n-grams: 
    # key = n-gram, 
    # value = the amount of times it appears
    def generate_hash(self, ngrams: list) -> list:
        result = dict()
        for ngram in ngrams:
            if ngram in result:
                result[ngram] += 1
            else:
                result[ngram] = 1
        return result