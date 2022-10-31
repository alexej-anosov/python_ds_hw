class CountVectorizer(object):
    def __init__(self):
        self.__tokens = []
        self.__num_of_tokens = len(self.__tokens)


    def __tokenize(self, corpus):
        """
        we get a list of unique words of the text that we get in fit_transform method
        and length of this list as properties of class instance
        """
        not_unique_tokens = []
        for string in corpus:
            not_unique_tokens.extend(map(lambda x: x.lower(), string.split()))
        for token in not_unique_tokens:
            if token not in self.__tokens:
                self.__tokens.append(token)
        self.__num_of_tokens = len(self.__tokens)


    def get_feature_names(self):
        """
        print unique words list
        """
        return self.__tokens


    def fit_transform(self, corpus):
        """
        we get the text(List of string), tokenize it,
        count how many times each word occurs in each string
        and return document-term matrix as list of lists
        """
        self.__tokenize(corpus)
        output = []
        for string in corpus:
            string_output = [0]*self.__num_of_tokens
            for index, word in enumerate(string.split()):
                i = 0
                while word.lower() != self.__tokens[i]:
                    i += 1
                string_output[i] += 1
            output.append(string_output)
        return output


text = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

if __name__ == '__main__':
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(text)
    print(vectorizer.get_feature_names())
    print(count_matrix)
