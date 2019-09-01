import numpy as np
import time
import os


class Word:

    def __init__(self, word, translate):
        self.answer = 0
        self.word = word
        self.translate = translate

    def checkTranslate(self, w):
        if w == self.translate:
            self.answer += 1
            return True
        else: return False


class ListWords:

    L = []

    def __init__(self, path):
        self.fileToList(path)

    def fileToList(self, path):
        f = open(path, 'r')
        line = f.readline()
        while line:
            word, translate = line[:-1].split(' - ')
            self.L.append(Word(word, translate))
            line = f.readline()
        f.close()

    def sortWords(self):
        L0 = list(filter(lambda x: x.answer == 0, self.L))
        L1 = list(filter(lambda x: x.answer == 1, self.L))
        L2 = list(filter(lambda x: x.answer == 2, self.L))
        self.L.clear()
        np.random.shuffle(L0)
        np.random.shuffle(L1)
        np.random.shuffle(L2)
        self.L.extend(L0)
        self.L.extend(L1)
        self.L.extend(L2)



if __name__ == '__main__':
    print('Enter path: ')
    a = ListWords(input())
    while len(ListWords.L) > 0:
        for i in a.L:
            print('word: ' + i.word)
            if i.checkTranslate(input('Enter translate: ')):
                print('grats')
            else:
                print('Right answer: ' + i.translate)
            input()
        a.sortWords()
