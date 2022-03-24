# Bust'em Plagiarism

An utility which finds similar texts.

Uses [N-gram model](https://en.wikipedia.org/wiki/N-gram)
(also known as
[bag-of-words](https://en.wikipedia.org/wiki/Bag-of-words_model) for N = 1
or [w-shingles](https://en.wikipedia.org/wiki/W-shingling) for N > 1) and text normalization (lower case, no punctuation, only stems leaved, etc.).

## Installation

### As a dependency

    pip3 install https://github.com/sprkweb/bustem-plagiarism/releases/download/v0.1/bustem_plagiarism-0.1.0-py3-none-any.whl

### How to build

    git clone https://github.com/sprkweb/bustem-plagiarism.git
    pip install -r requirements.txt

## API

    from bustem import BustEmIndex, plaintext_from_editorjs

    # n = the number of words in a phrase which is considered plagiarized
    index = BustEmIndex(language='english', n=1)

    # optional: get plain text from an EditorJS markup
    text = plaintext_from_editorjs(json.loads(...))

    # add some text for future comparision.
    # `meta` can be any associated data, e.g. id
    index.add(meta, text)
    index.add(meta2, text2)

    # check text for plagiarism from the first two texts.
    # each text is scored on a scale from 0 to 1, where 1 = same text.
    # it shows results only for the texts with similarity above threshold.
    # it will compare only indexed texts for which the filter is True.
    index.check(text3, threshold=0.2, filter=lambda meta: meta != 3)

## Example

Let's say you've got a JSON array of students' works in EditorJS format.

    [
        {
            "id": 1,
            "task": 76,
            "author": 159,
            "answer": "some EditorJS markup..."
        },
        ...
    ]

So, you want to find if some of them copied each other's works.

    from datetime import datetime
    import json
    from bustem import BustEmIndex, plaintext_from_editorjs

    start_time = datetime.now()

    with open('data.json', 'r') as f:
        works = json.load(f)

    index = BustEmIndex(language='russian', n=5)
    print("Identificator format: (submission, author, task)")
    for work in works:
        meta = (work['id'], work['author'], work['task'])

        text = plaintext_from_editorjs(json.loads(work['answer']))

        # If author is the same, he can copy himself. 
        # Also we won't check task 88
        f = lambda meta: meta[1] != work['author'] and meta[2] != 88
        # Check!
        scores = index.check(text, threshold=0.1, filter_ = f)
        
        # Print only if similar works are found
        if len(scores) > 1:
            for score in scores:
                print(f'{meta}\t is similar to {score[0]}.' + 
                    f'\tSimilarity: {round(score[1], 3)}')

        # Add this work for comparision with the next works
        index.add(meta, text)

    exec_time = datetime.now() - start_time
    print(f'{len(works)} done in {exec_time}')

Result:

    Identificator format: (submission, author, task)
    (325, 86, 154)   is similar to (434, 141, 154). Similarity: 0.5
    (325, 86, 154)   is similar to (422, 141, 154). Similarity: 0.185
    (164, 95, 76)    is similar to (194, 165, 76).  Similarity: 0.122
    (164, 95, 76)    is similar to (184, 165, 76).  Similarity: 0.12
    (98, 108, 76)    is similar to (114, 111, 76).  Similarity: 0.201
    (98, 108, 76)    is similar to (100, 111, 76).  Similarity: 0.18
    (68, 111, 76)    is similar to (98, 108, 76).   Similarity: 0.139
    (68, 111, 76)    is similar to (177, 73, 76).   Similarity: 0.11
    475 done in 0:00:02.588679
