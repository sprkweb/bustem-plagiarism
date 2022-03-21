from .compare_ngrams import compare_ngrams
from .normalize_text import TextNormalizer
from .generate_ngrams import NGramsGenerator

class BustEmIndex:
    # N - the amount of words in a sentence which can be considered plagiared
    def __init__(self, language='english', n=1) -> None:
        self.index = []
        self.normalizer = TextNormalizer(language)
        self.ngrams_generator = NGramsGenerator(n)

    def add(self, identity, text: str) -> None:
        self.index.append((identity, self.__text_to_ngrams(text)))

    def check(self, text: str, threshold = 0) -> list:
        checked_ngrams = self.__text_to_ngrams(text)
        result = []
        for item in self.index:
            score = compare_ngrams(checked_ngrams, item[1])
            if score >= threshold:
                result.append((item[0], score))
        result.sort(reverse=True, key=lambda x: x[1])
        return result

    def __text_to_ngrams(self, text: str) -> list:
        words = self.normalizer.normalize(text)
        ngrams = self.ngrams_generator.generate(words)
        return set(ngrams)