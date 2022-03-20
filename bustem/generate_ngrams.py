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
    