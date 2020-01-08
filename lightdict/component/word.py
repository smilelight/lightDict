import json


class Word:
    def __init__(self, pattern, pinyin=None, mean=None, syns=None, ants=None, sims=None):
        assert type(pattern) == str
        assert len(pattern) >= 1
        self.pattern = pattern
        if pinyin:
            self.pinyin = pinyin.split(';')
        self.mean = mean
        if syns:
            self.syns = syns.split(',')
        else:
            self.syns = []
        if ants:
            self.ants = ants.split(',')
        else:
            self.ants = []
        if sims:
            self.sims = sims.split(',')
        else:
            self.sims = []

    def __eq__(self, other):
        if type(other) == str:
            return self.pattern == other
        if type(other) == Word:
            assert type(other) == Word
            return self.pattern == other.pattern

    def __str__(self):
        return json.dumps({
            'word': self.pattern,
            'pinyin': self.pinyin,
            'syns': self.syns,
            'ants': self.ants,
            'sims': self.sims
        }, ensure_ascii=False, indent=1)
