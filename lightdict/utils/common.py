def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if '\u4e00' <= uchar <= '\u9fff':
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_chinese('哈'))
    print(is_chinese('a'))
