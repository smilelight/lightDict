import json

from ..utils.common import is_chinese


class Character:
    def __init__(self, pattern, pinyin=None, mean=None):
        assert type(pattern) == str
        assert len(pattern) == 1
        assert is_chinese(pattern)
        self.pattern = pattern
        self.pinyin = pinyin
        self.mean = mean

    def __eq__(self, other):
        if type(other) == str:
            return self.pattern == other
        if type(other) == Character:
            assert type(other) == Character
            return self.pattern == other.pattern

    def __str__(self):
        return json.dumps({
            'pattern': self.pattern,
            'pinyin': self.pinyin,
            'mean': self.mean
        }, ensure_ascii=False, indent=1)
