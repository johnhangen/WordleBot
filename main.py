#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.textReader import TextReader, wordsToList
from src.wordlePos import WordlePos


def main():
    reader = TextReader(path='data/words.txt')
    with reader.read() as lines:
       words = wordsToList(lines)
    
    WP = WordlePos(words)
    WP.find_words()
    words = WP.get_words()

    print(words)


if __name__ == '__main__':
    main()
