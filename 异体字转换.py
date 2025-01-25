from package.异体字字典 import 异体字字典 as d
from random import choice


def 异体字转换(s):
    res = []
    for _ in range(5):
        temp = []
        for c in s:
           temp.append(choice(d.get(c, c)))
        res.append(''.join(temp))
    return res


if __name__ == '__main__':
    s = input()
    res = 异体字转换(s)
    print('\n'.join(res))