class CountVectorizer(object):
    def __init__(self):
        self.tokens = []
        self.num_of_tokens = len(self.tokens)

    """we get a list of unique words of the text that we get in fit_transform method 
    and length of this list
    as properties of class instance"""
    def tokenize(self, corpus):
        for string in corpus:
            self.tokens.extend(map(lambda x: x.lower(), string.split()))
        self.tokens = list(set(self.tokens))
        self.num_of_tokens = len(self.tokens)

    """print unique words list"""
    def get_feature_names(self):
        return self.tokens

    """we get the text(List of string), 
    tokenize it,
    count how many times each word occurs in each string
    and return document-term matrix as list of lists"""
    def fit_transform(self, corpus):
        self.tokenize(corpus)
        output = []
        for string in corpus:
            string_output = [0]*self.num_of_tokens
            for index, word in enumerate(string.split()):
                i = 0
                while word.lower() != self.tokens[i]:
                    i += 1
                string_output[i] += 1
            output.append(string_output)
        return output


text = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(text)
print(vectorizer.get_feature_names())
print(count_matrix)

