#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager
import logging
from typing import Generator


class TextReader:
    """
    A class to read text from a file using a context manager.
    """
    def __init__(self, path : str) -> None:
        self.path = path

    @contextmanager
    def read(self, mode: str = 'r', encoding: str = 'utf-8') -> Generator[str, None, None]:
        """
        Context manager to read a file. Yields the file content.
        """
        try:
            with open(self.path, mode, encoding=encoding) as file:
                yield file.readlines()
        except FileNotFoundError:
            logging.error(f"File not found: {self.path}")
            yield ''
        except PermissionError:
            logging.error(f"Permission denied for file: {self.path}")
            yield ''
        except Exception as e:
            logging.error(f"Error reading file {self.path}: {e}")
            yield ''

    @staticmethod
    def wordsToList(lines: str) -> list:
        words = []
        for line in lines:
                words.append(line.strip())

        return words
