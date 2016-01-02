import random

START='_START_'
END='_END_'
PUNCT=['.',',',';',':','?','!']

class Markoff(object):

    def __init__(self,path=None,start_token=START,end_token=END):
        """
        path: A string, indicating the phrase file to read from and write to
        start_token: A string, used internally for denoting the start of phrases
        end_token: A string, used internally for denoting the end of phrases
        """
        if type(path) != str and path != None:
            raise TypeError('path must be a string if provided')

        self._chainmap = {}
        self._excluded_words = []
        self._path = path
        self._start = start_token
        self._end = end_token

        if self._path:
            try:
                f = open(self._path)
                text = f.read()
                for line in text.split('\n'):
                    self.add_vocab(line,False)
            except IOError:
                print('\'' + self._file + '\' does not exist, creating it now.')
                f = open(self._path,'w')
            finally:
                f.close()

    def add_vocab(self,text,write_to_file=True):
        """
        Adds word pairings from 'text' into markoff's memory
        """
        if type(text) != str:
            raise TypeError('text must be a string')

        if self._path and write_to_file:
            with open(self._path,'a') as f:
                f.write(text+'\n')

        prev_word = self._start

        for word in text.split():
            for token in self._split_punct(word): 
                try:
                    self._chainmap[prev_word].append(token)
                    if prev_word == '.':
                        self._chainmap[self._start].append(token)
                except Exception:
                    self._chainmap[prev_word] = [token]

                prev_word=token

        try:
            self._chainmap[prev_word].append(self._end)
        except Exception:
            self._chainmap[prev_word] = [self._end]
        
    def _nextWord(self,word):
        """
        Probablistically calculates next word
        """
        index = random.randint(0,len(self._chainmap[word])-1)
        return self._chainmap[word][index]

    def _split_punct(self,word):
        """
        Splits puntuated words into seperate tokens
        """
        result = []
        for p in PUNCT:
            ind = word.find(p)
            if ind >= 0:
                result.append(word[0:ind])
                result.append(word[ind:])
                return result
        result.append(word)
        return result

    def gen_sentence(self,max_length=None):
        """
        Generates a gen_sentence.  If max_length is provided, it generates a
        new gen_sentence until it is within length constraints
        """
        satisfactory = False

        while not satisfactory:
            word=self._nextWord(self._start)
            msg = ''
             
            while word != self._end:
                # Add space before all mid-sentence words
                if len(msg) != 0 and not word in PUNCT:
                    msg += ' '
                msg += word
                word = self._nextWord(word)
            if len(msg) > 0 and not max_length or len(msg) <= max_length:
                satisfactory = True

        return msg
