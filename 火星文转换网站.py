import requests_html, re


class Translate:
    hxw = 火星文 = 'hxw'

    def __init__(self):
        self.session = requests_html.HTMLSession()
        self.headers = {}

    def translate(self, text: str, method: str) -> list[str] | None:
        self.headers['user-agent'] = requests_html.UserAgent().random
        match method:
            case 'hxw':
                return self._translate2hxw(text)
            case _:
                ...

    def _translate2hxw(self, text: str) -> list[str]:
        params = {'wm': text}
        response = self.session.get('https://www.qiwangming.com/jsjs/process-fzl.php', params=params, headers=self.headers)
        res = re.findall(r'<textarea id="foo\d+" >(.*?)</textarea>', response.text)
        return res

if __name__ == '__main__':
    t = Translate()
    print(t.translate('我阐释你的梦', t.火星文))