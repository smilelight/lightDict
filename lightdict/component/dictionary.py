from abc import ABC, abstractmethod
import gc
import csv
import os


from .word import Word
from .character import Character


def check_file_type(file_name, file_type):
    assert type(file_name) == str
    if not file_name.endswith('.' + file_type):
        raise Exception('the file type must be {}'.format(file_type))


class Dictionary(ABC):
    def __init__(self, file_name, keep=True):
        self._file_name = file_name
        self._keep = keep
        if self._keep:
            if not os.path.isfile(self._file_name):
                raise FileNotFoundError
            else:
                self._dict = self._load(self._file_name)
        else:
            self._dict = None

    @abstractmethod
    def _load(self, file_name):
        raise NotImplementedError

    def __enter__(self):
        if self._dict is None:
            self._dict = self._load(self._file_name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._keep:
            self._dict = None
            gc.collect()

    def __getitem__(self, item):
        return self._get_item(item)

    @abstractmethod
    def _get_item(self, item):
        raise NotImplementedError

    def __contains__(self, item):
        if item in self._dict:
            return True
        return False


class HanziDict(Dictionary):
    """
    dictionary which contains Chinese characters
    """
    def _load(self, file_name):
        check_file_type(file_name, 'csv')
        dic = dict()
        with open(file_name, encoding='utf-8') as f:
            f_csv = csv.reader(f)
            headers = next(f_csv)
            assert len(headers) == 3
            for row in f_csv:
                dic[row[0]] = {
                    'pinyin': row[1],
                    'meaning': row[2]
                }
        return dic

    def _get_item(self, item):
        if self._dict is None:
            raise Exception('the HanziDict must be used as Context Manager if the parameter keep is False')
        if item in self._dict:
            return Character(item, self._dict[item]['pinyin'], self._dict[item]['meaning'])
        return None


class WordDict(Dictionary):
    """
    dictionary which contains Chinese words
    """
    def _load(self, file_name):
        check_file_type(file_name, 'csv')
        dic = dict()
        with open(file_name, encoding='utf-8') as f:
            f_csv = csv.reader(f)
            headers = next(f_csv)
            assert len(headers) == 6
            for row in f_csv:
                dic[row[0]] = {
                    'pinyin': row[1],
                    'meaning': row[2],
                    'syns': row[3],
                    'ants': row[4],
                    'sims': row[5]
                }
        return dic

    def _get_item(self, item):
        if self._dict is None:
            raise Exception('the WordDict must be used as Context Manager if the parameter keep is False')
        if item in self._dict:
            return Word(item, self._dict[item]['pinyin'], self._dict[item]['meaning'],
                        self._dict[item]['syns'], self._dict[item]['ants'], self._dict[item]['sims'])
        return None


# class SynSet(Dictionary):
#     """
#     dictionary which contains Chinese synonym sets
#     """
#     pass







