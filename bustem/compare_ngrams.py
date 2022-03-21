# Returns a score from 0 to 1: How similar are the documents?
# Score is the size of intersection of sets divided by the size of their union.
def compare_ngrams(ngrams1: set, ngrams2: set) -> int:
    return len(ngrams1.intersection(ngrams2)) / len(ngrams1.union(ngrams2))