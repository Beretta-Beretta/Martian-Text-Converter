from package.火星文字典 import *
import random

def 火星文转换(text, symbol=True):
    '''
    :param text: 需要转换的文本。
    :param symbol: 是否加符号。
    :return: 转换后的文本。
    '''
    def _火星文转换(s, symbol):
        '''
        :param s: 需要转换的单行文本。
        :param symbol: 是否加符号。
        :return: 转换后的文本。
        '''
        trans = []
        # 有组合字的先转换成组合字
        for _ in 组合字.keys():
            if _ in s:
                s = s.replace(_, random.choice(组合字[_]))

        # 逐字转换为火星文
        for c in s:
            if c == ' ' and symbol:     # 若需要添加符号，则将空格转换为符号
                trans.append(random.choice(符号))
            elif 火星文字典.get(c, []):      # 有对应火星文的就转换
                trans.append(random.choice(火星文字典[c]))
            else:
                trans.append(c)

        # 随机取符号
        fh = random.sample(符号, 3)

        return fh[0] + ''.join(trans) + ''.join(fh[1:]) if symbol else ''.join(trans)

    text = text.split('\n')
    return '\n'.join(_火星文转换(s, symbol) for s in text)


def 获取汉字对应火星文(c):
    assert len(c) == 1, '请输入单个字符。'
    try:
        return ' '.join(火星文字典[c])
    except KeyError:
        return ''


if __name__ == '__main__':
    while (s := input()):
        for i in range(5):
            print(火星文转换(s, False))