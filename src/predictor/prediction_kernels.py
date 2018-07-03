import re

class PredictionKernel:
    def predict(self, partial):
        raise NotImplementedError()

    def accept(self, label):
        raise NotImplementedError()

    def reject(self, label):
        raise NotImplementedError()

def _ngrams(text, n, character=False):
    if character:
        tokens = list(text)
    else:
        tokens = re.split(r"\W+", text)

    ngrams = set()

    for i in range(len(tokens) - n):
        # TODO Should probably include ngrams of N or less not just N
        ngrams.add(tuple(tokens[i : i + n]))

    return ngrams


def _ngrams_from_dataframe(df, n, character=False):
    # TODO trim vocabulary. For any reasonable corpus this will be too large
    ngrams = set()
    for column in df.columns:
        if isinstance(df[column][0], str):
            for r in df[column].values():
                ngrams.extend(_ngrams(r, n, character))
    return ngrams


class NgramWeightKernel(PredictionKernel):
    def __init__(self, parent, ngram_length, corpus):
        self._parent = parent
        self._ngram_length = ngram_length
        self.vocabulary = _ngrams_from_dataframe(corpus)
        self.labels = set()

    def predict(self, partial):
        raise NotImplementedError()

    def accept(self, label):
        

    def reject(self, label):
        raise NotImplementedError()
