import re
import nltk
import string
import html
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

# thanks https://gist.github.com/lvngd/3695aac64461de2cfb9d50bb11d5fbb3
class TextNormalizer:
    def __init__(self, language='english'):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stemmer = SnowballStemmer(language)
        self.punctuation = string.punctuation
        self.stop_words = set(stopwords.words(language))
        self.remove_tags = re.compile('<.*?>') 

    # Generate an array of normalized stems from a text
    def normalize(self, text: str) -> list:
        normalized_text = re.sub(self.remove_tags, '', text)
        normalized_text = html.unescape(normalized_text)
        normalized_text = normalized_text.lower()
        # divide into words
        words = word_tokenize(normalized_text)
        # leave only stems and remove stopwords
        words = [self.stemmer.stem(word) for word in words if self.__accept_word(word)]
        return words

    def __accept_word(self, word: str) -> bool:
        return word not in self.stop_words and word not in self.punctuation
