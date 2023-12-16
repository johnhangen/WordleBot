#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.textReader import TextReader, wordsToList
from src.const import letter_values


def sort_value(word: str) -> int:
    return sum(letter_values.get(letter, 0) for letter in set(word.lower()))



class WordlePos:
    def __init__(self, words: list[str]) -> None:
        self.real_letters = ['_', '_', 'o', '_', 'e']
        self.not_pos = {
            0: [],  
            1: [],     
            2: [],
            3: ['l'],
            4: []
        }
        self.not_letters = ['a', 'r', 'n', 'c', 't', 'i', 's', 'w', 'h']
        self.words = words

    def update_real_letters(self, letters: str) -> None:
        """Updates the correct letters."""
        self.real_letters = list(letters)

    def update_not_pos(self, letters: str, positions: list[int]) -> None:
        """Updates the misplaced letters and their positions."""
        self.not_pos = {pos: list(letters) for pos in positions}
    
    def update_not_letters(self, letters: str) -> None:
        """Updates the absent letters."""
        self.not_letters = list(letters)

    def find_words(self) -> None:
        """Filters words based on the set criteria."""
        self.words = [word for word in self.words if self.is_valid_word(word)]

    def is_valid_word(self, word: str) -> bool:
        """Check if a word is valid based on the set criteria."""
        if any(letter != '_' and word[i] != letter for i, letter in enumerate(self.real_letters)):
            return False

        for pos, letters in self.not_pos.items():
            for letter in letters:
                if word[pos] == letter or letter not in word:
                    return False                      

        if any(letter in word for letter in self.not_letters):
            return False

        return True

    def get_words(self) -> list[str]:
        """Returns the filtered list of words."""
        self.words.sort(key=sort_value, reverse=True)
        return self.words
